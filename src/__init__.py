"""Compatibility layer exposing the project as the legacy 'src' package."""
from importlib import import_module as _import_module
import sys as _sys

_pkg = _import_module("personal_agent")
_sys.modules[__name__] = _pkg
