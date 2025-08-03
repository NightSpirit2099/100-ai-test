"""Orquestrador central que coordena múltiplas estratégias de execução."""

import logging
from typing import Dict

from ..strategies.basic_strategy import BasicStrategy
from ..strategies.research_strategy import ResearchStrategy
from .interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


class MetaOrchestrator:
    """Orquestrador que analisa requisições e delega entre múltiplas estratégias."""

    def __init__(self, keyword_map: Dict[str, tuple[str, ...]] | None = None) -> None:
        """Inicializa o orquestrador com estratégias e mapa de palavras-chave.

        Args:
            keyword_map: Mapeamento configurável de identificadores de estratégia
                para tuplas de palavras-chave. Se não fornecido, um conjunto
                padrão é utilizado.
        """

        self.strategies: Dict[str, IExecutionStrategy] = {
            "basic": BasicStrategy(),
            "research": ResearchStrategy(),
        }
        self.keyword_map: Dict[str, tuple[str, ...]] = keyword_map or {
            "research": ("research", "pesquisa"),
            "basic": ("basic",),
        }

    def analyze_request(self, request: UserRequest) -> str:
        """Analisa a requisição do usuário para determinar a estratégia.

        A análise identifica a primeira estratégia com palavra-chave presente no
        texto. Caso nenhuma palavra-chave seja encontrada, a estratégia
        ``basic`` é utilizada como padrão.

        Args:
            request: Requisição enviada pelo usuário.

        Returns:
            Identificador da estratégia a ser utilizada.
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
            identificador. Se nenhuma estratégia corresponder ao
            identificador informado, a estratégia ``basic`` é utilizada e um
            aviso é registrado no log.
        """
        try:
            return self.strategies[analysis]
        except KeyError:
            logger.warning("Estratégia desconhecida: %s. Utilizando 'basic'.", analysis)
            return self.strategies["basic"]

    def execute(self, request: UserRequest) -> AgentResponse:
        """Processa a requisição do usuário e retorna a resposta do agente.

        Args:
            request: Requisição do usuário a ser processada.

        Returns:
            Resposta do agente gerada pela estratégia selecionada.
        """
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
