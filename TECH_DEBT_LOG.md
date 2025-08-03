# Tech Debt Log

Registre aqui decisões técnicas que requerem revisões futuras ou potenciais refatorações.

## Entradas

- *[2024-05-10]* Estrutura inicial do `system_config` definida de forma simples; poderá ser expandida para suportar hierarquias de equipes e permissões.

## [2025-08-03] Versionamento mínimo de dependências críticas
**Localização**: `requirements.txt`
**Descrição**: Definidas versões mínimas estáveis para Pydantic (>=2.7,<3) e PyYAML (>=6.0,<7) visando garantir compatibilidade e previsibilidade.
**Refatoração Planejada**: Reavaliar limites ao surgir nova versão principal das dependências.
**Responsável**: @ai_assistant

