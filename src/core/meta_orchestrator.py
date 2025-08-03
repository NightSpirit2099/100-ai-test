from .interfaces import IExecutionStrategy, UserRequest


class MetaOrchestrator:
    """Orquestrador principal responsável por coordenar estratégias de execução."""

    def analyze_request(self, request: UserRequest):
        """Analisa a requisição do usuário para extrair intenções."""
        raise NotImplementedError

    def select_strategy(self, analysis) -> IExecutionStrategy:
        """Seleciona a estratégia apropriada com base na análise."""
        raise NotImplementedError
