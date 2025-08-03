import logging

from src.core.interfaces import AgentResponse, UserRequest

logger = logging.getLogger(__name__)


class SampleAgent:
    """Agente de exemplo que ecoa o texto do usuário."""

    def run(self, request: UserRequest) -> AgentResponse:
        """Processa a requisição do usuário e retorna uma resposta."""
        logger.info("SampleAgent received request: %s", request.text)
        response = AgentResponse(text=f"Echo: {request.text}")
        logger.info("SampleAgent response: %s", response.text)
        return response
