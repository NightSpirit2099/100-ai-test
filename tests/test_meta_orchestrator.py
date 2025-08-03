import logging
from typing import Iterable
import pytest

from src.core.interfaces import AgentResponse, UserRequest
from src.core.meta_orchestrator import MetaOrchestrator
from src.strategies.basic_strategy import BasicStrategy
from src.strategies.research_strategy import ResearchStrategy
from src.utils.logging import LOG_FORMAT


def _get_configured_handler(handlers: Iterable[logging.Handler]) -> logging.Handler:
    return next(h for h in handlers if getattr(h.formatter, "_fmt", "") == LOG_FORMAT)


def test_meta_orchestrator_basic_strategy(caplog: pytest.LogCaptureFixture) -> None:
    orchestrator = MetaOrchestrator()
    request = UserRequest(text="teste básico")

    with caplog.at_level(logging.INFO):
        analysis = orchestrator.analyze_request(request)
        strategy = orchestrator.select_strategy(analysis)
        response = orchestrator.execute(request)

    assert analysis == "basic"
    assert isinstance(strategy, BasicStrategy)
    assert isinstance(response, AgentResponse)
    assert "Processed" in response.text

    handler = _get_configured_handler(logging.getLogger().handlers)
    record = next(r for r in caplog.records if r.message == "Processamento da requisição concluído")
    formatted = handler.format(record)
    assert formatted == "INFO - src.core.meta_orchestrator - Processamento da requisição concluído"


def test_meta_orchestrator_research_strategy() -> None:
    orchestrator = MetaOrchestrator()
    request = UserRequest(text="please research about AI")

    analysis = orchestrator.analyze_request(request)
    assert analysis == "research"

    strategy = orchestrator.select_strategy(analysis)
    assert isinstance(strategy, ResearchStrategy)

    response = orchestrator.execute(request)
    assert isinstance(response, AgentResponse)
    assert "Researching" in response.text

