# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later

import importlib
import pkgutil

import pystatpower


def test_public_exported() -> None:
    """Test that all subpackages and modules are exported in the parent's `__init__.py`."""

    missing_exports = []

    for _, module_name, _ in pkgutil.walk_packages(pystatpower.__path__, prefix=f"{pystatpower.__name__}."):
        if any(part.startswith("_") for part in module_name.split(".")):
            continue

        parts = module_name.split(".")
        parent_name = ".".join(parts[:-1])
        child_name = parts[-1]

        parent_module = importlib.import_module(parent_name)
        parent_all = getattr(parent_module, "__all__", [])

        if child_name not in parent_all:
            missing_exports.append(f"{module_name}")

        assert not missing_exports, (
            "The following public modules/subpackages are not exported in the parent package's __init__.py:\n"
            + "\n".join(missing_exports)
        )
