"""Estratégias de pesquisa de informações."""

import logging

from ..core.interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


class ResearchStrategy(IExecutionStrategy):
    """Estratégia que simula a pesquisa de informações."""

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia retornando uma resposta de pesquisa.

        Args:
            request: Requisição do usuário com o tema da pesquisa.

        Returns:
            Resposta contendo o texto que simula o resultado da pesquisa.
        """
        logger.info("Executando ResearchStrategy")
        return AgentResponse(text=f"Researching: {request.text}")
