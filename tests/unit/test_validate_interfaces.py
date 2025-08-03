from __future__ import annotations

from scripts import validate_interfaces


def test_validate_interfaces_main_returns_zero() -> None:
    assert validate_interfaces.main() == 0
