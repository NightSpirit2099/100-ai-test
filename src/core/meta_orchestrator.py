import logging

from .interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


class MetaOrchestrator:
    """Orquestrador principal responsável por coordenar estratégias de execução."""

    def analyze_request(self, request: UserRequest):
        """Analisa a requisição do usuário para extrair intenções."""
        raise NotImplementedError

    def select_strategy(self, analysis) -> IExecutionStrategy:
        """Seleciona a estratégia apropriada com base na análise."""
        raise NotImplementedError

    def execute(self, request: UserRequest) -> AgentResponse:
        """Processa a requisição do usuário e retorna a resposta do agente."""
        logger.info("Iniciando processamento da requisição do usuário")

        logger.debug("Analisando a requisição")
        analysis = self.analyze_request(request)
        logger.debug("Análise concluída: %s", analysis)

        logger.debug("Selecionando estratégia")
        strategy = self.select_strategy(analysis)
        logger.debug(
            "Estratégia selecionada: %s", strategy.__class__.__name__
        )

        logger.debug("Executando estratégia")
        response = strategy.execute(request)
        logger.debug("Execução concluída: %s", response)

        logger.info("Processamento da requisição concluído")
        return response
