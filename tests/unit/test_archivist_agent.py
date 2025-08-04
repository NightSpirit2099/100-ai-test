from __future__ import annotations

import logging
import pytest

from personal_agent.agents.archivist_agent import ArchivistAgent
from personal_agent.core.interfaces import AgentResponse, UserRequest


def test_archivist_agent_execute_returns_expected_response(
    caplog: pytest.LogCaptureFixture,
) -> None:
    agent = ArchivistAgent()
    request = UserRequest(text="data to archive")

    with caplog.at_level(logging.INFO):
        response = agent.execute(request)

    assert isinstance(response, AgentResponse)
    assert response.text == "Archived: data to archive"
    assert "Executando ArchivistAgent" in caplog.text
