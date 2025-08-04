from __future__ import annotations

import logging
import pytest

from personal_agent.memory.simple_rag import SimpleRAG


def test_add_documents_stores_texts(caplog: pytest.LogCaptureFixture) -> None:
    rag = SimpleRAG()
    texts = ["First doc", "Second Doc"]

    with caplog.at_level(logging.INFO):
        rag.add_documents(texts)

    assert rag._docs == texts
    assert "Added 2 documents" in caplog.text

def test_query_returns_semantic_matches() -> None:
    rag = SimpleRAG()
    rag.add_documents([
        "The cat sat on the mat",
        "Dogs are friendly",
        "Cats and kittens are cute",
    ])

    results = rag.query("cat", top_k=2)

    assert results == [
        "The cat sat on the mat",
        "Cats and kittens are cute",
    ]
