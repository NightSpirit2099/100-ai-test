import logging
from typing import Dict

from ..strategies.basic_strategy import BasicStrategy
from .interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


class MetaOrchestrator:
    """Orquestrador responsável por analisar requisições e delegar estratégias.

    Atualmente registra apenas :class:`BasicStrategy`,
    utilizada como estratégia padrão para qualquer requisição recebida.
    """

    def __init__(self) -> None:
        """Inicializa o orquestrador registrando as estratégias disponíveis."""
        self.strategies: Dict[str, IExecutionStrategy] = {
            "basic": BasicStrategy(),
        }

    def analyze_request(self, request: UserRequest) -> str:
        """Analisa a requisição do usuário para determinar a estratégia.

        A análise mínima identifica palavras-chave simples no texto da
        requisição. Caso nenhuma palavra-chave seja encontrada, a estratégia
        ``basic`` é utilizada como padrão.
        """

        text = request.text.lower()
        if "basic" in text:
            return "basic"
        return "basic"

    def select_strategy(self, analysis: str) -> IExecutionStrategy:
        """Seleciona a estratégia apropriada com base na análise.

        Args:
            analysis: Identificador retornado por :meth:`analyze_request`.

        Returns:
            Implementação de :class:`IExecutionStrategy` associada ao
            identificador.

        Raises:
            ValueError: Se nenhuma estratégia corresponder ao identificador
                informado.
        """

        try:
            return self.strategies[analysis]
        except KeyError as exc:  # pragma: no cover - defensive branch
            raise ValueError(f"Estratégia desconhecida: {analysis}") from exc

    def execute(self, request: UserRequest) -> AgentResponse:
        """Processa a requisição do usuário e retorna a resposta do agente."""
        logger.info("Iniciando processamento da requisição do usuário")

        logger.debug("Analisando a requisição")
        analysis = self.analyze_request(request)
        logger.debug("Análise concluída: %s", analysis)

        logger.debug("Selecionando estratégia")
        strategy = self.select_strategy(analysis)
        logger.debug("Estratégia selecionada: %s", strategy.__class__.__name__)

        logger.debug("Executando estratégia")
        response = strategy.execute(request)
        logger.debug("Execução concluída: %s", response)

        logger.info("Processamento da requisição concluído")
        return response
