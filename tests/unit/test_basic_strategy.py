from __future__ import annotations

import logging
from typing import Iterable
import pytest

from src.core.interfaces import AgentResponse, UserRequest
from src.strategies.basic_strategy import BasicStrategy
from src.utils.logging import LOG_FORMAT


def _get_configured_handler(handlers: Iterable[logging.Handler]) -> logging.Handler:
    return next(h for h in handlers if getattr(h.formatter, "_fmt", "") == LOG_FORMAT)


def test_basic_strategy_execute_returns_expected_response(caplog: pytest.LogCaptureFixture) -> None:
    strategy = BasicStrategy()
    request = UserRequest(text="example")

    with caplog.at_level(logging.INFO):
        response = strategy.execute(request)

    assert isinstance(response, AgentResponse)
    assert response.text == "Processed: example"

    handler = _get_configured_handler(logging.getLogger().handlers)
    record = next(r for r in caplog.records if r.message == "Executando BasicStrategy")
    formatted = handler.format(record)
    assert formatted == "INFO - src.strategies.basic_strategy - Executando BasicStrategy"

