import pytest
from pydantic import ValidationError

from personal_agent.core.interfaces import AgentResponse, UserRequest


def test_user_request_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        UserRequest(text="hello", unexpected="field")  # type: ignore[call-arg]


def test_agent_response_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        AgentResponse(text="hi", extra="value")  # type: ignore[call-arg]
