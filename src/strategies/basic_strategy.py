import logging
from typing import final

from ..core.interfaces import AgentResponse, UserRequest

logger = logging.getLogger(__name__)


@final
class BasicStrategy:
    """Estratégia simples de execução.

    Utilizada como implementação mínima de :class:`IExecutionStrategy`.
    """

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia retornando uma resposta padrão."""
        logger.info("Executando BasicStrategy")
        return AgentResponse(text=f"Processed: {request.text}")

