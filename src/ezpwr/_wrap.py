# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

from collections.abc import Callable

from scipy.optimize import brentq

from .exceptions import SolutionNotFoundError


def _wrap_brentq(f: Callable[..., float], a: float, b: float, args: tuple = ()) -> float:
    """A wrapper for brentq from the Scipy package."""
    if f(a, *args) * f(b, *args) >= 0:
        raise SolutionNotFoundError

    return float(brentq(f, a, b, args=args))
