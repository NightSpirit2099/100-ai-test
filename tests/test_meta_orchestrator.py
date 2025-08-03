from src.core.interfaces import AgentResponse, UserRequest
from src.core.meta_orchestrator import MetaOrchestrator
from src.strategies.basic_strategy import BasicStrategy
from src.strategies.research_strategy import ResearchStrategy


def test_meta_orchestrator_basic_strategy() -> None:
    strategies = {"basic": BasicStrategy()}
    orchestrator = MetaOrchestrator(strategies=strategies)
    request = UserRequest(text="teste básico")

    analysis = orchestrator.analyze_request(request)
    assert analysis == "basic"

    strategy = orchestrator.select_strategy(analysis)
    assert isinstance(strategy, BasicStrategy)

    response = orchestrator.execute(request)
    assert isinstance(response, AgentResponse)
    assert "Processed" in response.text


def test_meta_orchestrator_research_strategy() -> None:
    strategies = {"research": ResearchStrategy()}
    orchestrator = MetaOrchestrator(strategies=strategies)
    request = UserRequest(text="please research about AI")

    analysis = orchestrator.analyze_request(request)
    assert analysis == "research"

    strategy = orchestrator.select_strategy(analysis)
    assert isinstance(strategy, ResearchStrategy)

    response = orchestrator.execute(request)
    assert isinstance(response, AgentResponse)
    assert "Researching" in response.text
