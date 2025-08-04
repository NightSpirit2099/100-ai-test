"""Ensure packages can be imported without side effects."""

import importlib
from typing import List

import pytest


MODULES: List[str] = [
    "personal_agent",
    "personal_agent.core",
    "personal_agent.agents",
    "personal_agent.strategies",
    "personal_agent.tools",
    "personal_agent.memory",
    "personal_agent.utils",
    "personal_agent.adapters",
]


@pytest.mark.parametrize("module_name", MODULES)
def test_import_module(module_name: str) -> None:
    """Import a module by name to verify it loads correctly."""
    importlib.import_module(module_name)
