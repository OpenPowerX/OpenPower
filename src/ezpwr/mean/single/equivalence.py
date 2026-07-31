# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Power analysis for the equivalence test of a single mean.

This module provides functions to calculate or estimate the following parameters:

- statistical power
- sample size
"""

from math import ceil
from math import sqrt
from typing import Literal

from scipy.stats import t

from ..._math_utils import _owen_o4
from ..._wrap import _wrap_brentq as brentq
from ._power import _power as _raw_power


def _power(
    mean: float,
    lower_equivalence_limit: float,
    upper_equivalence_limit: float,
    std: float,
    size: float,
    alpha: float,
    dist: Literal["z", "t"],
) -> float:
    """Calculate the statistical power."""
    if dist == "z" or (dist == "t" and size > 300):
        return (
            _raw_power(mean - lower_equivalence_limit, std, size, "greater", alpha, dist)
            + _raw_power(mean - upper_equivalence_limit, std, size, "less", alpha, dist)
            - 1
        )
    else:
        df = size - 1
        t1 = t.ppf(1 - alpha, df)
        t2 = -t1
        delta1 = (mean - lower_equivalence_limit) * sqrt(size) / std
        delta2 = (mean - upper_equivalence_limit) * sqrt(size) / std
        power = _owen_o4(df, t1, t2, delta1, delta2)
        return power


def solve_power(
    *,
    mean: float,
    lower_equivalence_limit: float,
    upper_equivalence_limit: float,
    std: float,
    size: int,
    alpha: float = 0.025,
    dist: Literal["z", "t"] = "t",
) -> float:
    r"""Calculate the statistical power.

    Args:
        mean:
            Actual mean.
        lower_equivalence_limit:
            Lower equivalence limit, defined as the minimum mean value regarded as considered equivalent.
        upper_equivalence_limit:
            Upper equivalence limit, defined as the maximum mean value regarded as considered equivalent.
        std:
            Standard deviation.
        size:
            Sample size.
        alpha:
            Significance level.

            The equivalence test is a two one-sided test, with a significance level of 0.025 being commonly used.
        dist:
            The distribution used for the test.

            - `'z'`: Normal distribution.
            - `'t'`: Student's t distribution.

    Returns:
        The statistical power of the test.
    """
    return _power(mean, lower_equivalence_limit, upper_equivalence_limit, std, size, alpha, dist)


def solve_size(
    *,
    mean: float,
    lower_equivalence_limit: float,
    upper_equivalence_limit: float,
    std: float,
    alpha: float = 0.025,
    power: float = 0.8,
    dist: Literal["z", "t"] = "t",
) -> int:
    r"""Estimate the required sample size.

    Args:
        mean:
            Actual mean.
        lower_equivalence_limit:
            Lower equivalence limit, defined as the minimum mean value regarded as considered equivalent.
        upper_equivalence_limit:
            Upper equivalence limit, defined as the maximum mean value regarded as considered equivalent.
        std:
            Standard deviation.
        alpha:
            Significance level.

            The equivalence test is a two one-sided test, with a significance level of 0.025 being commonly used.
        power:
            Expected statistical power.

            0.8 is a commonly used value for statistical power.
        dist:
            The distribution used for the test.

            - `'z'`: Normal distribution.
            - `'t'`: Student's t distribution.

    Returns:
        The required sample size.
    """

    def func(size: float) -> float:
        return _power(mean, lower_equivalence_limit, upper_equivalence_limit, std, size, alpha, dist) - power

    return ceil(brentq(func, 1 + 0.1, 1e12))
