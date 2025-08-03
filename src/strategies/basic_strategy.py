from ..core.interfaces import AgentResponse, IExecutionStrategy, UserRequest
from ..utils.logging import get_logger

logger = get_logger(__name__)


class BasicStrategy:
    """Estratégia simples de execução.

    Utilizada como implementação mínima de :class:`IExecutionStrategy`.
    """

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia retornando uma resposta padrão."""
        logger.info("Executando BasicStrategy")
        return AgentResponse(text=f"Processed: {request.text}")

