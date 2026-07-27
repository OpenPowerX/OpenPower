# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Power analysis for a single mean.

This package provides the following modules:

- ci: Confidence intervals for a single mean.
- inequality: Inequality tests for a single mean.
- noninferiority: Non-inferiority tests for a single mean.
- superiority: Superiority tests for a single mean.
- equivalence: Equivalence tests for a single mean.
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
