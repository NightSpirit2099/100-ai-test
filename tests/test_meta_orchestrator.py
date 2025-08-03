import yaml

from config_models import SystemConfig
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


def test_meta_orchestrator_research_synonyms_spanish_french() -> None:
    orchestrator = MetaOrchestrator()

    request_es = UserRequest(text="Necesito investigación sobre IA")
    assert orchestrator.analyze_request(request_es) == "research"

    request_fr = UserRequest(text="Peux-tu faire une recherche sur l'IA?")
    assert orchestrator.analyze_request(request_fr) == "research"


def test_meta_orchestrator_custom_keywords_from_config() -> None:
    with open("system_config.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    config = SystemConfig.from_dict(data)

    orchestrator_default = MetaOrchestrator()
    request_it = UserRequest(text="Poderia fazer uma ricerca sobre IA?")
    assert orchestrator_default.analyze_request(request_it) == "basic"

    orchestrator_config = MetaOrchestrator(keyword_map=config.keyword_map)
    assert orchestrator_config.analyze_request(request_it) == "research"

