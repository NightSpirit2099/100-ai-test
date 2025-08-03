from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class LLMProfile(BaseModel):
    provider: str = Field(..., description="LLM service provider identifier")
    model: str = Field(..., description="Model name or identifier")
    temperature: Optional[float] = Field(
        0.0, ge=0.0, le=1.0, description="Sampling temperature for the model"
    )


class Agent(BaseModel):
    description: str = Field(..., description="Short description of the agent's purpose")
    llm: str = Field(..., description="Key of the LLM profile used by this agent")


class Task(BaseModel):
    description: str = Field(..., description="Description of what the task does")
    agent: str = Field(..., description="Name of the agent responsible for the task")


class Team(BaseModel):
    agents: List[str] = Field(..., description="List of agent names that compose the team")


class SystemConfig(BaseModel):
    llm_profiles: Dict[str, LLMProfile]
    agents: Dict[str, Agent]
    tasks: Dict[str, Task]
    teams: Dict[str, Team]

    @classmethod
    def from_dict(cls, data: Dict) -> "SystemConfig":
        """Parse a raw dict (e.g. loaded from YAML) into a SystemConfig."""
        return cls(**data)
