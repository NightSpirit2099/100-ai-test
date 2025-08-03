from ..core.interfaces import AgentResponse, IExecutionStrategy, UserRequest
from ..utils.logging import get_logger

logger = get_logger(__name__)


class ResearchStrategy:
    """Estratégia que simula a pesquisa de informações."""

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia retornando uma resposta de pesquisa."""
        logger.info("Executando ResearchStrategy")
        return AgentResponse(text=f"Researching: {request.text}")
