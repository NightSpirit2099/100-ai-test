from __future__ import annotations

import logging
from pathlib import Path

import pytest

from personal_agent.memory.simple_rag import SimpleRAG


def test_add_documents_stores_texts(
    caplog: pytest.LogCaptureFixture, tmp_path: Path
) -> None:
    rag = SimpleRAG(persist_directory=str(tmp_path))
    texts = ["First doc", "Second Doc"]

    with caplog.at_level(logging.INFO):
        rag.add_documents(texts)

    results = rag.query("First doc", top_k=2)
    assert "Added 2 documents" in caplog.text
    assert "First doc" in results


def test_query_returns_matching_docs_case_insensitive(tmp_path: Path) -> None:
    rag = SimpleRAG(persist_directory=str(tmp_path))
    rag.add_documents(["Python is great", "I love coding", "PYTHON typing"])

    results = rag.query("python", top_k=2)

    assert set(results) == {"Python is great", "PYTHON typing"}
