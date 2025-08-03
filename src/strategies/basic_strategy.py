import logging

from ..core.interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


class BasicStrategy(IExecutionStrategy):
    """Estratégia simples de execução.

    Utilizada como implementação mínima de :class:`IExecutionStrategy`.
    """

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia retornando uma resposta padrão."""
        logger.info("Executando BasicStrategy")
        return AgentResponse(text=f"Processed: {request.text}")
