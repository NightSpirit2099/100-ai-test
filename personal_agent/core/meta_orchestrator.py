"""Meta-orquestrador que direciona requisições para estratégias adequadas.

Ele escolhe entre ``BasicStrategy`` para interações diretas,
``ResearchStrategy`` quando a solicitação exige um passo de investigação
mais profundo e ``ArchivistAgent`` para operações de arquivamento ou
recuperação de memória.
"""

from typing import Dict

from ..agents.archivist_agent import ArchivistAgent
from ..strategies.basic_strategy import BasicStrategy
from ..strategies.research_strategy import ResearchStrategy
from .interfaces import AgentResponse, IExecutionStrategy, UserRequest
import logging

logger = logging.getLogger(__name__)


class MetaOrchestrator:
    """Analisa requisições e delega para ``BasicStrategy``,
    ``ResearchStrategy`` ou ``ArchivistAgent`` conforme necessário."""

    def __init__(self) -> None:
        """Inicializa o orquestrador registrando as estratégias disponíveis.

        Inclui ``BasicStrategy`` para tarefas diretas,
        ``ResearchStrategy`` para solicitações que demandam pesquisa
        adicional e ``ArchivistAgent`` para requisições relacionadas a
        arquivamento de informações.
        """
        self.strategies: Dict[str, IExecutionStrategy] = {
            "basic": BasicStrategy(),
            "research": ResearchStrategy(),
            "archivist": ArchivistAgent(),
        }

    def analyze_request(self, request: UserRequest) -> str:
        """Analisa a requisição do usuário para determinar a estratégia.

        A análise identifica palavras-chave simples no texto para decidir
        entre ``ResearchStrategy``, ``ArchivistAgent`` ou ``BasicStrategy``.
        Se nenhuma palavra for encontrada, ``BasicStrategy`` é utilizada como
        padrão.

        Args:
            request: Requisição enviada pelo usuário.

        Returns:
            Identificador da estratégia a ser utilizada.
        """
        text = request.text.lower()
        if any(keyword in text for keyword in ("research", "pesquisa")):
            return "research"
        if any(keyword in text for keyword in ("archive", "arquivar", "memoria", "memory")):
            return "archivist"
        if "basic" in text:
            return "basic"
        return "basic"

    def select_strategy(self, analysis: str) -> IExecutionStrategy:
        """Seleciona a estratégia apropriada com base na análise.

        Args:
            analysis: Identificador retornado por :meth:`analyze_request`.

        Returns:
            Implementação de :class:`IExecutionStrategy` associada ao
            identificador. Se nenhuma estratégia corresponder ao
            identificador informado, ``BasicStrategy`` é utilizada e um aviso
            é registrado no log.
        """
        try:
            return self.strategies[analysis]
        except KeyError:
            logger.warning("Estratégia desconhecida: %s. Utilizando 'basic'.", analysis)
            return self.strategies["basic"]

    def execute(self, request: UserRequest) -> AgentResponse:
        """Processa a requisição e executa a estratégia selecionada.

        Args:
            request: Requisição do usuário a ser processada.

        Returns:
            Resposta do agente gerada por ``BasicStrategy`` ou
            ``ResearchStrategy`` conforme definido pela análise.
        """
        logger.info("Iniciando processamento da requisição do usuário")

        logger.debug("Analisando a requisição")
        analysis = self.analyze_request(request)
        logger.debug("Análise concluída: %s", analysis)

        logger.debug("Selecionando estratégia")
        strategy = self.select_strategy(analysis)
        logger.debug("Estratégia selecionada: %s", strategy.__class__.__name__)

        logger.debug("Executando estratégia")
        try:
            response = strategy.execute(request)
        except Exception as exc:  # pragma: no cover - logging tested separately
            logger.error(
                "Erro ao executar a estratégia %s: %s",
                strategy.__class__.__name__,
                exc,
            )
            raise
        logger.debug("Execução concluída: %s", response)

        logger.info("Processamento da requisição concluído")
        return response
