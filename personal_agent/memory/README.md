# SimpleRAG Memory Module

`SimpleRAG` fornece um armazenamento persistente baseado em ChromaDB para experimentos de Retrieval-Augmented Generation (RAG).
Ele utiliza um modelo da biblioteca [`sentence-transformers`](https://www.sbert.net) para gerar embeddings e realiza busca semântica sobre os documentos.

## Limitações Atuais
- Ausência de metadados avançados ou controle de concorrência.
- Dependência direta do ChromaDB para persistência.
- Ausência de otimizações para grandes volumes de dados.

## Plano de Evolução
1. **Iteração atual:** utilizar ChromaDB para busca semântica com embeddings `all-MiniLM-L6-v2`.
2. **Iteração 3:** migrar para uma memória híbrida Grafo-Vetor baseada em Neo4j, conforme descrito no [Plano de Arquitetura](../../Plano_de_arquitetura.md).
3. Integrar um `ArchivistAgent` para gerenciar ingestão, versionamento e poda de documentos.

Detalhes adicionais sobre as fases estão no [Plano de Execução](../../Plano_de_execucao.md).

## Uso Básico
```python
from src.memory import SimpleRAG

rag = SimpleRAG()
rag.add_documents(["Python é ótimo", "Eu adoro programar"])
resultados = rag.query("python", top_k=1)
```

O módulo é destinado apenas a protótipos e será substituído conforme o roadmap de evolução.
