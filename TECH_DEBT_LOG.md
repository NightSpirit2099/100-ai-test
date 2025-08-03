# Tech Debt Log

Registre aqui decisões técnicas que requerem revisões futuras ou potenciais refatorações.

## Entradas

- *[2024-05-10]* Estrutura inicial do `system_config` definida de forma simples; poderá ser expandida para suportar hierarquias de equipes e permissões.

## [2025-08-03] Stub temporário para SimpleRAG
**Localização**: `src/memory/simple_rag.py`
**Descrição**: Classe `SimpleRAG` criada como interface mínima, sem integração com banco vetorial ou grafo.
**Refatoração Planejada**: Iteração futura para conectar ChromaDB e Neo4j.
**Responsável**: @arquiteto_principal
