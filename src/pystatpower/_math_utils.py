# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

"""A module containing mathematical tool functions."""

from math import exp
from math import inf
from math import log
from math import pi
from math import sqrt
from typing import TypeAlias

from scipy.integrate import quad
from scipy.special import gammaln
from scipy.stats import nct
from scipy.stats import norm
from scipy.stats import t

Domain: TypeAlias = tuple[float, float]


def _domain_square_root_of_quad(a: float, b: float, c: float, /) -> Domain | tuple[Domain, Domain] | float | None:
    r"""Solve the domain of the function f(x) = \sqrt{ax^2+bx+c} (a ≠ 0)."""
    delta = b**2 - 4 * a * c
    if a > 0:
        if delta <= 0:
            return -inf, inf
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            return ((-inf, x1), (x2, inf))
    else:  # a < 0
        if delta < 0:
            return None
        elif delta == 0:
            return -b / (2 * a)
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            return x2, x1


def _owen_q1(df: float, t_val: float, delta: float, r: float) -> float:
    """The Owen's Q1 function."""

    def _integrand(x: float) -> float:
        """The Owen's integrand."""
        log_c = 1 / 2 * log(2 * pi) - gammaln(df / 2) - (df - 2) / 2 * log(2)
        log_kernal = norm.logcdf(t_val * x / sqrt(df) - delta) + (df - 1) * log(x) + norm.logpdf(x)
        return exp(log_c + log_kernal)

    # Gaussian sampling at the peak
    peak = sqrt(max(df - 1, 1.0))
    pts = [peak] if peak < r else []

    result, _ = quad(_integrand, 0, r, points=pts)
    return result


def _owen_q2(df: float, t_val: float, delta: float, r: float) -> float:
    """The Owen's Q2 function."""
    return nct.cdf(t_val, df, delta) - _owen_q1(df, t_val, delta, r)


def _owen_o1(df: float, t1_val: float, t2_val: float, delta1: float, delta2: float) -> float:
    """The Owen's equality (8)."""
    if delta1 < delta2:
        return t.cdf(t2_val, df)

    a1 = t1_val / sqrt(df)
    a2 = t2_val / sqrt(df)
    r = (delta1 - delta2) / (a1 - a2)
    return _owen_q1(df, t1_val, delta1, r) + _owen_q2(df, t2_val, delta2, r)


def _owen_o2(df: float, t1_val: float, t2_val: float, delta1: float, delta2: float) -> float:
    """The Owen's equality (9)."""
    if delta1 < delta2:
        return t.cdf(t1_val, df) - t.cdf(t2_val, df)

    a1 = t1_val / sqrt(df)
    a2 = t2_val / sqrt(df)
    r = (delta1 - delta2) / (a1 - a2)
    return _owen_q2(df, t1_val, delta1, r) - _owen_q2(df, t2_val, delta2, r)


def _owen_o3(df: float, t1_val: float, t2_val: float, delta1: float, delta2: float) -> float:
    """The Owen's equality (10)."""
    if delta1 < delta2:
        return 1 - t.cdf(t1_val, df)

    a1 = t1_val / sqrt(df)
    a2 = t2_val / sqrt(df)
    r = (delta1 - delta2) / (a1 - a2)
    return 1 - _owen_q2(df, t1_val, delta1, r) - _owen_q1(df, t2_val, delta2, r)


def _owen_o4(df: float, t1: float, t2: float, delta1: float, delta2: float) -> float:
    """The Owen's equality (11)."""
    if delta1 < delta2:
        return 0.0

    a1 = t1 / sqrt(df)
    a2 = t2 / sqrt(df)
    r = (delta1 - delta2) / (a1 - a2)
    return _owen_q1(df, t2, delta2, r) - _owen_q1(df, t1, delta1, r)
