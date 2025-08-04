"""Simple RAG implementation backed by a persistent ChromaDB collection."""

from __future__ import annotations

import logging
import uuid
from typing import List, Sequence

import chromadb
from chromadb.utils.embedding_functions import EmbeddingFunction
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class _SentenceTransformerEmbedding(EmbeddingFunction):
    """Embedding function using a shared SentenceTransformer model."""

    def __init__(self, model: SentenceTransformer) -> None:
        self._model = model

    def __call__(self, texts: Sequence[str]) -> List[List[float]]:  # type: ignore[override]
        return self._model.encode(list(texts)).tolist()


class SimpleRAG:
    """ChromaDB-backed RAG implementation."""

    def __init__(self, persist_directory: str = ".chromadb") -> None:
        """Initialize the RAG system.

        Args:
            persist_directory: Directory used by ChromaDB to persist data.
        """
        self._model = SentenceTransformer("all-MiniLM-L6-v2")
        self._client = chromadb.PersistentClient(path=persist_directory)
        embedding_fn = _SentenceTransformerEmbedding(self._model)
        self._collection = self._client.get_or_create_collection(
            name="simple_rag", embedding_function=embedding_fn
        )
        logger.debug("SimpleRAG initialized at %s", persist_directory)

    def add_documents(self, texts: List[str]) -> None:
        """Ingest a batch of documents into the memory store.

        Args:
            texts: Raw text documents to embed and persist.
        """
        embeddings = self._model.encode(texts).tolist()
        ids = [str(uuid.uuid4()) for _ in texts]
        self._collection.add(documents=texts, embeddings=embeddings, ids=ids)
        logger.info("Added %d documents", len(texts))

    def query(self, question: str, top_k: int = 5) -> List[str]:
        """Retrieve relevant documents for a given question.

        Args:
            question: Natural language query.
            top_k: Number of results to return.

        Returns:
            List of document snippets ranked by similarity.
        """
        result = self._collection.query(query_texts=[question], n_results=top_k)
        documents = result.get("documents", [[]])[0]
        logger.debug("Query for '%s' returned %d documents", question, len(documents))
        return documents
