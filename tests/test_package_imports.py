"""Ensure packages can be imported without side effects."""

import importlib
from typing import List

import pytest


MODULES: List[str] = [
    "src",
    "src.core",
    "src.agents",
    "src.strategies",
    "src.tools",
    "src.memory",
    "src.utils",
    "src.adapters",
]


@pytest.mark.parametrize("module_name", MODULES)
def test_import_module(module_name: str) -> None:
    """Import a module by name to verify it loads correctly."""
    importlib.import_module(module_name)
