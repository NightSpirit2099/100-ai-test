from __future__ import annotations

import logging
from typing import Iterable
import pytest

from src.core.interfaces import AgentResponse, UserRequest
from src.strategies.research_strategy import ResearchStrategy
from src.utils.logging import LOG_FORMAT


def _get_configured_handler(handlers: Iterable[logging.Handler]) -> logging.Handler:
    return next(h for h in handlers if getattr(h.formatter, "_fmt", "") == LOG_FORMAT)


def test_research_strategy_execute_returns_expected_response(
    caplog: pytest.LogCaptureFixture,
) -> None:
    strategy = ResearchStrategy()
    request = UserRequest(text="example research")

    with caplog.at_level(logging.INFO):
        response = strategy.execute(request)

    assert isinstance(response, AgentResponse)
    assert response.text == "Researching: example research"

    handler = _get_configured_handler(logging.getLogger().handlers)
    record = next(r for r in caplog.records if r.message == "Executando ResearchStrategy")
    formatted = handler.format(record)
    assert formatted == "INFO - src.strategies.research_strategy - Executando ResearchStrategy"

