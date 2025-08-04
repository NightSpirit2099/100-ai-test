"""
Stub module for a simple Retrieval-Augmented Generation (RAG) system.

This module defines the minimal interface for future memory integration.
It exposes the SimpleRAG class, an in-memory placeholder that stores documents
and returns basic matches for a query. Initial versions use ChromaDB for vector
storage and retrieval, with plans to incorporate Neo4j for graph-based
relationships in later iterations.
"""

from typing import List
import logging

logger = logging.getLogger(__name__)


class SimpleRAG:
    """In-memory placeholder for a RAG implementation."""

    def __init__(self) -> None:
        """Initialize the RAG system."""
        self._docs: List[str] = []
        logger.debug("SimpleRAG initialized")

    def add_documents(self, texts: List[str]) -> None:
        """Ingest a batch of documents into the memory store.

        Args:
            texts: Raw text documents to embed and persist.
        """
        self._docs.extend(texts)
        logger.info("Added %d documents", len(texts))

    def query(self, question: str, top_k: int = 5) -> List[str]:
        """Retrieve relevant documents for a given question.

        Args:
            question: Natural language query.
            top_k: Number of results to return.

        Returns:
            List of document snippets containing the query.
        """
        lowered = question.lower()
        matches = [doc for doc in self._docs if lowered in doc.lower()]
        return matches[:top_k]
