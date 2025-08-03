from __future__ import annotations

import logging
import pytest

from personal_agent.core.interfaces import AgentResponse, UserRequest
from personal_agent.strategies.basic_strategy import BasicStrategy


def test_basic_strategy_execute_returns_expected_response(caplog: pytest.LogCaptureFixture) -> None:
    strategy = BasicStrategy()
    request = UserRequest(text="example")

    with caplog.at_level(logging.INFO):
        response = strategy.execute(request)

    assert isinstance(response, AgentResponse)
    assert response.text == "Processed: example"
    assert "Executando BasicStrategy" in caplog.text
