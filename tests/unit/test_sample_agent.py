from __future__ import annotations

import logging
import pytest

from src.core.interfaces import AgentResponse, UserRequest
from src.agents.sample_agent import SampleAgent


def test_sample_agent_run_returns_expected_response(
    caplog: pytest.LogCaptureFixture,
) -> None:
    agent = SampleAgent()
    request = UserRequest(text="hello")

    with caplog.at_level(logging.INFO):
        response = agent.run(request)

    assert isinstance(response, AgentResponse)
    assert response.text == "Echo: hello"
    assert "SampleAgent received request: hello" in caplog.text
    assert "SampleAgent response: Echo: hello" in caplog.text
