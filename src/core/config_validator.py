from __future__ import annotations

from typing import Any

from pydantic import ValidationError

from config_models import SystemConfig


class ConfigValidator:
    """Validate cross references in a SystemConfig instance."""

    def __init__(self, config: SystemConfig) -> None:
        self._config = config

    def validate(self) -> None:
        """Validate configuration, raising ValidationError on issues."""
        errors: list[dict[str, Any]] = []

        for agent_name, agent in self._config.agents.items():
            if agent.llm not in self._config.llm_profiles:
                msg = f"Unknown llm profile '{agent.llm}' for agent '{agent_name}'"
                errors.append(
                    {
                        "type": "value_error",
                        "loc": ("agents", agent_name, "llm"),
                        "msg": msg,
                        "input": agent.llm,
                        "ctx": {"error": msg},
                    }
                )

        for task_name, task in self._config.tasks.items():
            if task.agent not in self._config.agents:
                msg = f"Unknown agent '{task.agent}' for task '{task_name}'"
                errors.append(
                    {
                        "type": "value_error",
                        "loc": ("tasks", task_name, "agent"),
                        "msg": msg,
                        "input": task.agent,
                        "ctx": {"error": msg},
                    }
                )

        for team_name, team in self._config.teams.items():
            for member in team.agents:
                if member not in self._config.agents:
                    msg = f"Team '{team_name}' references unknown agent '{member}'"
                    errors.append(
                        {
                            "type": "value_error",
                            "loc": ("teams", team_name, "agents"),
                            "msg": msg,
                            "input": member,
                            "ctx": {"error": msg},
                        }
                    )

        if errors:
            raise ValidationError.from_exception_data("SystemConfig", errors)
