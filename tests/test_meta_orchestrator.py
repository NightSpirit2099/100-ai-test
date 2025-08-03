from src.core.interfaces import AgentResponse, UserRequest
from src.core.meta_orchestrator import MetaOrchestrator
from src.strategies.basic_strategy import BasicStrategy


def test_meta_orchestrator_flow() -> None:
    orchestrator = MetaOrchestrator()
    request = UserRequest(text="teste básico")

    analysis = orchestrator.analyze_request(request)
    assert analysis == "basic"

    strategy = orchestrator.select_strategy(analysis)
    assert isinstance(strategy, BasicStrategy)

    response = orchestrator.execute(request)
    assert isinstance(response, AgentResponse)
    assert "Processed" in response.text

