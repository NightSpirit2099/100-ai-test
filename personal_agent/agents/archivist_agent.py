"""Agent dedicated to managing archival operations."""

import logging

from ..core.interfaces import AgentResponse, IExecutionStrategy, UserRequest

logger = logging.getLogger(__name__)


class ArchivistAgent(IExecutionStrategy):
    """Simulates archiving and retrieving information."""

    def execute(self, request: UserRequest) -> AgentResponse:
        """Archive the provided text and return a confirmation.

        Args:
            request: User request containing the text to be archived.

        Returns:
            Response acknowledging the archival action.
        """
        logger.info("Executando ArchivistAgent")
        return AgentResponse(text=f"Archived: {request.text}")
