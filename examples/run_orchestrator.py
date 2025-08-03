"""Run a simple MetaOrchestrator demo.

This script loads the system configuration, validates it using
:class:`ConfigValidator` and starts a minimal interactive loop where the
user can type a prompt and receive the orchestrator's response.
"""

from __future__ import annotations

from typing import Any

import yaml

from config_models import SystemConfig
from personal_agent.core.config_validator import ConfigValidator
from personal_agent.core.interfaces import UserRequest
from personal_agent.core.meta_orchestrator import MetaOrchestrator


def load_config(path: str) -> SystemConfig:
    """Load and validate a :class:`SystemConfig` from ``path``."""
    with open(path, encoding="utf-8") as file:
        data: dict[str, Any] = yaml.safe_load(file)
    config = SystemConfig.from_dict(data)
    ConfigValidator(config).validate()
    return config


def main() -> None:
    """Entry point for running the orchestrator demo."""
    config = load_config("system_config.yaml")
    print(f"Loaded config version {config.version}")
    orchestrator = MetaOrchestrator()

    user_input = input("Digite sua pergunta: ")
    request = UserRequest(text=user_input)
    response = orchestrator.execute(request)
    print(response.text)


if __name__ == "__main__":
    main()
