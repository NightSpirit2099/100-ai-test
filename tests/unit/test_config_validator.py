from __future__ import annotations

import pytest
import yaml
from pydantic import ValidationError

from config_models import SystemConfig
from src.core.config_validator import ConfigValidator


def load_config(path: str) -> SystemConfig:
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return SystemConfig.from_dict(data)


def test_validate_valid_config() -> None:
    config = load_config("system_config.yaml")
    validator = ConfigValidator(config)
    validator.validate()  # should not raise
    assert config.version == "1.0"


def test_validate_invalid_references() -> None:
    data = {
        "version": "1.0",
        "llm_profiles": {"default": {"provider": "gemini", "model": "gemini-pro"}},
        "agents": {"researcher": {"description": "desc", "llm": "missing"}},
        "tasks": {
            "t": {"description": "desc", "agent": "ghost"}
        },
        "teams": {"default": {"agents": ["ghost"]}},
    }
    config = SystemConfig.from_dict(data)
    validator = ConfigValidator(config)
    with pytest.raises(ValidationError) as exc:
        validator.validate()
    message = str(exc.value)
    assert "missing" in message
    assert "ghost" in message
