# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Power analysis for two independent proportions.

This package provides the following modules:

- ci: Confidence intervals for two independent proportions.
- inequality: Inequality tests for two independent proportions.
- noninferiority: Non-inferiority tests for two independent proportions.
- superiority: Superiority tests for two independent proportions.
"""

from . import ci
from . import inequality
from . import noninferiority
from . import superiority

__all__ = [
    "ci",
    "inequality",
    "noninferiority",
    "superiority",
]
