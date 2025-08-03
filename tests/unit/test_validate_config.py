from __future__ import annotations

import logging
from pathlib import Path

import pytest

from validate_config import main


def test_main_nonexistent_path_returns_error(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.ERROR):
        result = main("nonexistent.yaml")
    assert result == 1
    assert "Arquivo não encontrado" in caplog.text


def test_main_malformed_yaml_returns_error(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    bad_yaml = tmp_path / "bad.yaml"
    bad_yaml.write_text("foo: [bar", encoding="utf-8")
    with caplog.at_level(logging.ERROR):
        result = main(str(bad_yaml))
    assert result == 1
    assert "Erro ao ler YAML" in caplog.text
