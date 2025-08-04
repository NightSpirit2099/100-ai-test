# SimpleRAG Memory Module

`SimpleRAG` fornece um armazenamento em memória para experimentos iniciais de Retrieval-Augmented Generation (RAG).
Ele mantém uma lista de textos e realiza buscas por substring para recuperar documentos relevantes.

## Limitações Atuais
- Todo o conteúdo é mantido apenas em memória; não há persistência em disco.
- Busca ingênua por substring, sem embeddings ou ranking semântico.
- Ausência de metadados, controle de concorrência ou otimizações para grandes volumes.

## Plano de Evolução
1. **MVP:** conectar o módulo a um vector store simples (ChromaDB) para busca semântica.
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
