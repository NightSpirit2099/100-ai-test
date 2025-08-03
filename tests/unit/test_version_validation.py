from __future__ import annotations

import logging
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from config_models import SystemConfig
from validate_config import main as validate_main


def _load_base_config() -> dict:
    with open("system_config.yaml", "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def test_system_config_accepts_valid_version() -> None:
    data = _load_base_config()
    data["version"] = "2.1"
    config = SystemConfig.from_dict(data)
    assert config.version == "2.1"


def test_system_config_rejects_invalid_version() -> None:
    data = _load_base_config()
    data["version"] = "2"
    with pytest.raises(ValidationError):
        SystemConfig.from_dict(data)


def test_validate_config_reports_invalid_version(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    data = _load_base_config()
    data["version"] = "2"
    cfg_path = tmp_path / "config.yaml"
    with open(cfg_path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh)

    caplog.set_level(logging.ERROR)
    result = validate_main(str(cfg_path))
    assert result == 1
    assert "Versão inválida" in caplog.text
