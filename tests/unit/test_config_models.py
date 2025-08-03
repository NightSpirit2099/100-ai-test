from __future__ import annotations

import pytest
from pydantic import ValidationError

from config_models import LLMProfile, SystemConfig


def test_llm_profile_requires_positive_temperature() -> None:
    with pytest.raises(ValidationError):
        LLMProfile(provider="gemini", model="gemini-pro", temperature=0)


def test_system_config_rejects_non_positive_temperature() -> None:
    data = {
        "version": "1.0",
        "llm_profiles": {
            "default": {
                "provider": "gemini",
                "model": "gemini-pro",
                "temperature": -0.1,
            }
        },
        "agents": {},
        "tasks": {},
        "teams": {},
    }
    with pytest.raises(ValidationError):
        SystemConfig.from_dict(data)
