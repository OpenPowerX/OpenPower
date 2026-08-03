# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Power analysis for the equivalence test of two independent means.

This module provides functions to calculate or estimate the following parameters:

- statistical power
- sample size
"""

from math import sqrt
from typing import Literal

from scipy.stats import t

from ..._math_utils import _owen_o4
from ._power import _power as _raw_power
from ._verify import _verify_mean_and_get_diff
from ._verify import _verify_std_and_get_std


def _power(
    *,
    diff: float,
    lower_margin: float,
    upper_margin: float,
    treatment_std: float | None = None,
    reference_std: float | None = None,
    std: float | None = None,
    treatment_size: float,
    reference_size: float,
    alpha: float,
    dist: Literal["z", "t"],
    equal_var: bool,
    approx_t_method: Literal["welch", "satterthwaite"],
) -> float:

    match dist:
        case "z":
            return (
                _raw_power(
                    diff=diff,
                    margin=lower_margin,
                    treatment_std=treatment_std,
                    reference_std=reference_std,
                    std=std,
                    treatment_size=treatment_size,
                    reference_size=reference_size,
                    alpha=alpha,
                    dist=dist,
                    equal_var=equal_var,
                )
                + _raw_power(
                    diff=diff,
                    margin=upper_margin,
                    treatment_std=treatment_std,
                    reference_std=reference_std,
                    std=std,
                    treatment_size=treatment_size,
                    reference_size=reference_size,
                    alpha=alpha,
                    dist=dist,
                    equal_var=equal_var,
                )
                - 1
            )
        case "t":
            if equal_var:
                df = treatment_size + reference_size - 2
                se = sqrt(
                    ((treatment_size - 1) * treatment_std**2 + (reference_size - 1) * reference_std**2)
                    / df
                    * (1 / treatment_size + 1 / reference_size)
                )
                t1_val = t.ppf(1 - alpha, df)
                t2_val = t.ppf(alpha, df)
                nct1 = (diff - lower_margin) / se
                nct2 = (diff - upper_margin) / se
                return _owen_o4(df, t1_val, t2_val, nct1, nct2)
            else:  # equal_var == False
                se = sqrt(treatment_std**2 / treatment_size + reference_std**2 / reference_size)
                nct1 = (diff - lower_margin) / se
                nct2 = (diff - upper_margin) / se
                match approx_t_method:
                    case "welch":
                        df = (
                            se**4
                            / (
                                treatment_std**4 / (treatment_size**2 * (treatment_size + 1))
                                + reference_std**4 / (reference_size**2 * (reference_size + 1))
                            )
                            - 2
                        )
                        t1_val = t.ppf(1 - alpha, df)
                        t2_val = t.ppf(alpha, df)
                        return _owen_o4(df, t1_val, t2_val, nct1, nct2)
                    case "satterthwaite":
                        df = se**4 / (
                            treatment_std**4 / (treatment_size**2 * (treatment_size - 1))
                            + reference_std**4 / (reference_size**2 * (reference_size - 1))
                        )
                        t1_val = t.ppf(1 - alpha, df)
                        t2_val = t.ppf(alpha, df)
                        return _owen_o4(df, t1_val, t2_val, nct1, nct2)


def solve_power(
    *,
    treatment_mean: float | None = None,
    reference_mean: float | None = None,
    diff: float | None = None,
    lower_margin: float,
    upper_margin: float,
    treatment_std: float | None = None,
    reference_std: float | None = None,
    std: float | None = None,
    treatment_size: int,
    reference_size: int,
    alpha: float = 0.025,
    dist: Literal["z", "t"] = "t",
    equal_var: bool = False,
    approx_t_method: Literal["welch", "satterthwaite"] = "welch",
) -> float:
    r"""Calculate the statistical power.

    Args:
        treatment_mean:
            Mean in the treatment group.

            If `diff` is omitted, this parameter is required along with `reference_mean`.
        reference_mean:
            Mean in the reference group.

            If `diff` is omitted, this parameter is required along with `treatment_mean`.
        diff:
            Mean difference between treatment and reference group.

            If both `treatment_mean` and `reference_mean` are not specified, this parameter is required.
        lower_margin:
            The lower equivalence margin.

            !!! tip

                Regardless of whether you specify a positive or negative number, the program will internally convert it
                to the lower equivalent margin in standard negative form.
        upper_margin:
            The upper equivalence margin.

            !!! tip

                Regardless of whether you specify a positive or negative number, the program will internally convert it
                to the lower equivalent margin in standard positive form.
        treatment_std:
            Standard deviation in the treatment group.
        reference_std:
            Standard deviation in the reference group.
        std:
            Standard deviation in both groups.

            This is a convenience parameter that will override `treatment_std` and `reference_std` when `dist` is `z` and `equal_var` is `True`.

            If you specify `dist` as `z` and `equal_var` as `True`, you can just specify `std` instead of `treatment_std` and `reference_std`.
            Internally, the value of `std` will be treated as the standard deviation of both the treatment and reference groups.
        treatment_size:
            Sample size in the treatment group.
        reference_size:
            Sample size in the reference group.
        alpha:
            Significance level.

            The equivalence test is a two one-sided test, with a significance level of 0.025 being commonly used.
        dist:
            The distribution used for the test.

            - `'z'`: Standard normal distribution.
            - `'t'`: Student's or non-central t distribution.
        equal_var:
            Whether to assume equal variances between treatment and reference groups.

            - `True`: Variances are assumed equal.
            - `False`: Variances are assumed unequal.
        approx_t_method:
            Approximate t-test method. It is used when `dist` is `'t'` and `equal_var` = `False`.

            - `'welch'`: Welch's approximate t-test (1947).
            - `'satterthwaite'`: Satterthwaite's approximate t-test (1946).

    Returns:
        The statistical power of the test.

    Raises:
        ValueError: If all of `diff`, `treatment_mean` and `reference_mean` are omitted.
        ValueError: If `dist` is `z` and `equal_var` is `True`, and all `treatment_std`, `reference_std` and `std` is omitted.
        ValueError: If `dist` is `z` and `equal_var` is `True`, and both `treatment_std` and `reference_std` are provided, but they are not equal.
    """
    diff = _verify_mean_and_get_diff(treatment_mean, reference_mean, diff)
    std = _verify_std_and_get_std(treatment_std, reference_std, std, dist, equal_var)

    lower_margin = -abs(lower_margin)
    upper_margin = abs(upper_margin)

    return _power(
        diff=diff,
        lower_margin=lower_margin,
        upper_margin=upper_margin,
        treatment_std=treatment_std,
        reference_std=reference_std,
        std=std,
        treatment_size=treatment_size,
        reference_size=reference_size,
        alpha=alpha,
        dist=dist,
        equal_var=equal_var,
        approx_t_method=approx_t_method,
    )


# def solve_size(
#     *,
#     treatment_mean: float | None = None,
#     reference_mean: float | None = None,
#     diff: float | None = None,
#     lower_margin: float,
#     upper_margin: float,
#     treatment_std: float | None = None,
#     reference_std: float | None = None,
#     std: float | None = None,
#     ratio: float = 1,
#     alpha: float = 0.025,
#     power: float = 0.8,
#     dist: Literal["z", "t"] = "t",
#     equal_var: bool = False,
#     approx_t_method: Literal["welch", "satterthwaite"] = "welch",
# ) -> tuple[int, int]:
#     r"""Calculate the statistical power.

#     Args:
#         treatment_mean:
#             Mean in the treatment group.

#             If `diff` is omitted, this parameter is required along with `reference_mean`.
#         reference_mean:
#             Mean in the reference group.

#             If `diff` is omitted, this parameter is required along with `treatment_mean`.
#         diff:
#             Mean difference between treatment and reference group.

#             If both `treatment_mean` and `reference_mean` are not specified, this parameter is required.
#         lower_margin:
#             The lower equivalence margin.

#             !!! tip

#                 Regardless of whether you specify a positive or negative number, the program will internally convert it
#                 to the lower equivalent margin in standard negative form.
#         upper_margin:
#             The upper equivalence margin.

#             !!! tip

#                 Regardless of whether you specify a positive or negative number, the program will internally convert it
#                 to the lower equivalent margin in standard positive form.
#         treatment_std:
#             Standard deviation in the treatment group.
#         reference_std:
#             Standard deviation in the reference group.
#         std:
#             Standard deviation in both groups.

#             This is a convenience parameter that will override `treatment_std` and `reference_std` when `dist` is `z` and `equal_var` is `True`.

#             If you specify `dist` as `z` and `equal_var` as `True`, you can just specify `std` instead of `treatment_std` and `reference_std`.
#             Internally, the value of `std` will be treated as the standard deviation of both the treatment and reference groups.
#         ratio:
#             Ratio of sample sizes in the treatment and reference groups.
#         alpha:
#             Significance level.

#             The equivalence test is a two one-sided test, with a significance level of 0.025 being commonly used.
#         power:
#             Expected statistical power.

#             0.8 is a commonly used value for statistical power.
#         dist:
#             The distribution used for the test.

#             - `'z'`: Standard normal distribution.
#             - `'t'`: Student's or non-central t distribution.
#         equal_var:
#             Whether to assume equal variances between treatment and reference groups.

#             - `True`: Variances are assumed equal.
#             - `False`: Variances are assumed unequal.
#         approx_t_method:
#             Approximate t-test method. It is used when `dist` is `'t'` and `equal_var` = `False`.

#             - `'welch'`: Welch's approximate t-test (1947).
#             - `'satterthwaite'`: Satterthwaite's approximate t-test (1946).

#     Returns:
#         The statistical power of the test.

#     Raises:
#         ValueError: If all of `diff`, `treatment_mean` and `reference_mean` are omitted.
#         ValueError: If `dist` is `z` and `equal_var` is `True`, and all `treatment_std`, `reference_std` and `std` is omitted.
#         ValueError: If `dist` is `z` and `equal_var` is `True`, and both `treatment_std` and `reference_std` are provided, but they are not equal.
#     """
#     diff = _verify_mean_and_get_diff(treatment_mean, reference_mean, diff)
#     std = _verify_std_and_get_std(treatment_std, reference_std, std, dist, equal_var)

#     lower_margin = -abs(lower_margin)
#     upper_margin = abs(upper_margin)

#     if ratio >= 1:

#         def func(reference_size: float) -> float:
#             return (
#                 _power(
#                     diff=diff,
#                     lower_margin=lower_margin,
#                     upper_margin=upper_margin,
#                     treatment_std=treatment_std,
#                     reference_std=reference_std,
#                     std=std,
#                     treatment_size=reference_size * ratio,
#                     reference_size=reference_size,
#                     alpha=alpha,
#                     dist=dist,
#                     equal_var=equal_var,
#                     approx_t_method=approx_t_method,
#                 )
#                 - power
#             )

#         lb = max(1 + 1e-12, 3 / (1 + ratio))
#         ub = 1e12
#         reference_size = int(ceil(brentq(func, lb, ub)))
#         treatment_size = int(ceil(reference_size * ratio))
#         return treatment_size, reference_size
#     else:

#         def func(treatment_size: float) -> float:
#             return (
#                 _power(
#                     diff=diff,
#                     lower_margin=lower_margin,
#                     upper_margin=upper_margin,
#                     treatment_std=treatment_std,
#                     reference_std=reference_std,
#                     std=std,
#                     treatment_size=treatment_size,
#                     reference_size=treatment_size / ratio,
#                     alpha=alpha,
#                     dist=dist,
#                     equal_var=equal_var,
#                     approx_t_method=approx_t_method,
#                 )
#                 - power
#             )

#         lb = max(1 + 1e-12, 3 / (1 + 1 / ratio))
#         ub = 1e12
#         treatment_size = ceil(brentq(func, lb, ub))
#         reference_size = ceil(treatment_size / ratio)
#         return treatment_size, reference_size
