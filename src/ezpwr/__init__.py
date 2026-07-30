# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

"""ezpwr: Power Analysis Toolkit for Python.

Documentation is available in the docstrings and online at https://ezpwr.readthedocs.io/.
"""

from importlib.metadata import version

from . import correlation
from . import exceptions
from . import mean
from . import misc
from . import proportion

__version__ = version("ezpwr")

__all__ = [
    "exceptions",
    "correlation",
    "mean",
    "proportion",
    "misc",
]
