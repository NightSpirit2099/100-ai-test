from typing import Protocol

from pydantic import BaseModel


class UserRequest(BaseModel):
    """Representa uma requisição de um usuário para o sistema."""

    text: str

    model_config = {"extra": "forbid"}


class AgentResponse(BaseModel):
    """Representa a resposta gerada por um agente."""

    text: str

    model_config = {"extra": "forbid"}


class IExecutionStrategy(Protocol):
    """Contrato para estratégias de execução do Meta-Orquestrador."""

    def execute(self, request: UserRequest) -> AgentResponse:
        """Executa a estratégia baseada na requisição do usuário."""
        ...
