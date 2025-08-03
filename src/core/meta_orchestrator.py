import logging
from typing import Dict, List, Optional

from ..strategies.basic_strategy import BasicStrategy
from ..strategies.research_strategy import ResearchStrategy
from .interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


DEFAULT_KEYWORD_MAP: Dict[str, List[str]] = {
    "research": [
        "research",
        "pesquisa",
        "investigación",
        "investigacion",
        "recherche",
    ],
    "basic": ["basic", "básico", "basico", "basique"],
}


class MetaOrchestrator:
    """Orquestrador que analisa requisições e delega entre múltiplas estratégias."""

    def __init__(self, keyword_map: Optional[Dict[str, List[str]]] = None) -> None:
        """Inicializa o orquestrador registrando as estratégias disponíveis.

        Args:
            keyword_map: Mapeamento adicional de estratégias para palavras-chave.
                Palavras-chave fornecidas aqui são combinadas com ``DEFAULT_KEYWORD_MAP``.
        """

        self.strategies: Dict[str, IExecutionStrategy] = {
            "basic": BasicStrategy(),
            "research": ResearchStrategy(),
        }
        self.keyword_map = DEFAULT_KEYWORD_MAP.copy()
        if keyword_map:
            for strategy, keywords in keyword_map.items():
                self.keyword_map.setdefault(strategy, [])
                self.keyword_map[strategy].extend(k.lower() for k in keywords)

    def analyze_request(self, request: UserRequest) -> str:
        """Analisa a requisição do usuário para determinar a estratégia.

        A análise identifica palavras-chave simples no texto da requisição.
        Caso nenhuma palavra-chave seja encontrada, a estratégia ``basic`` é
        utilizada como padrão.
        """

        text = request.text.lower()
        for strategy, keywords in self.keyword_map.items():
            if any(keyword in text for keyword in keywords):
                return strategy
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
        except KeyError:
            logger.warning("Estratégia desconhecida: %s. Utilizando 'basic'.", analysis)
            return self.strategies["basic"]

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
