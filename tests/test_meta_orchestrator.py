import logging

from src.core.interfaces import AgentResponse, UserRequest
from src.core.meta_orchestrator import MetaOrchestrator
from src.strategies.basic_strategy import BasicStrategy
from src.strategies.research_strategy import ResearchStrategy


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


def test_select_strategy_unknown_defaults_to_basic(caplog) -> None:
    orchestrator = MetaOrchestrator()

    with caplog.at_level(logging.WARNING, logger="src.core.meta_orchestrator"):
        strategy = orchestrator.select_strategy("unknown")

    assert "Estratégia desconhecida" in caplog.text
    assert isinstance(strategy, BasicStrategy)

