import logging
import pytest

from personal_agent.core.interfaces import (
    AgentResponse,
    IExecutionStrategy,
    UserRequest,
)
from personal_agent.core.meta_orchestrator import MetaOrchestrator
from personal_agent.strategies.basic_strategy import BasicStrategy
from personal_agent.strategies.research_strategy import ResearchStrategy


def test_meta_orchestrator_basic_strategy() -> None:
    orchestrator = MetaOrchestrator()
    request = UserRequest(text="teste básico")

    analysis = orchestrator.analyze_request(request)
    assert analysis == "basic"

    strategy = orchestrator.select_strategy(analysis)
    assert isinstance(strategy, BasicStrategy)

    response = orchestrator.execute(request)
    assert isinstance(response, AgentResponse)
    assert "Processed" in response.text


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


def test_select_strategy_unknown_returns_basic_and_logs_warning(
    caplog: pytest.LogCaptureFixture,
) -> None:
    orchestrator = MetaOrchestrator()
    with caplog.at_level(logging.WARNING):
        strategy = orchestrator.select_strategy("inexistente")

    assert isinstance(strategy, BasicStrategy)
    assert any(
        record.levelno == logging.WARNING
        and "Estratégia desconhecida" in record.getMessage()
        for record in caplog.records
    )


def test_execute_logs_and_reraises_on_strategy_error(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Verifica que erros da estratégia são registrados e propagados."""

    class FailingStrategy(IExecutionStrategy):
        def execute(self, request: UserRequest) -> AgentResponse:
            raise RuntimeError("falha simulada")

    orchestrator = MetaOrchestrator()
    orchestrator.strategies["basic"] = FailingStrategy()
    request = UserRequest(text="teste básico")

    with caplog.at_level(logging.ERROR):
        with pytest.raises(RuntimeError):
            orchestrator.execute(request)

    assert any(
        record.levelno == logging.ERROR
        and "FailingStrategy" in record.getMessage()
        and "falha simulada" in record.getMessage()
        for record in caplog.records
    )
