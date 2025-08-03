import logging
from typing import final

from ..core.interfaces import AgentResponse, UserRequest

logger = logging.getLogger(__name__)


@final
class ResearchStrategy:
    """Estratégia que simula a pesquisa de informações."""

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia retornando uma resposta de pesquisa."""
        logger.info("Executando ResearchStrategy")
        return AgentResponse(text=f"Researching: {request.text}")
