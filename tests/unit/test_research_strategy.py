from __future__ import annotations

import logging
import pytest

from personal_agent.core.interfaces import AgentResponse, UserRequest
from personal_agent.strategies.research_strategy import ResearchStrategy


def test_research_strategy_execute_returns_expected_response(
    caplog: pytest.LogCaptureFixture,
) -> None:
    strategy = ResearchStrategy()
    request = UserRequest(text="example research")

    with caplog.at_level(logging.INFO):
        response = strategy.execute(request)

    assert isinstance(response, AgentResponse)
    assert response.text == "Researching: example research"
    assert "Executando ResearchStrategy" in caplog.text
