# 100-ai-test

Projeto de exemplo para o sistema de Meta-Orquestração.

## Visão Geral

Repositório que demonstra um agente pessoal multi-agente, onde um Meta-Orquestrador coordena agentes especializados. A arquitetura está organizada em:

- `core/` – Orquestrador e abstrações centrais
- `strategies/` – Implementações de `IExecutionStrategy`
- `agents/` – Agentes especializados (ex.: `ArchivistAgent`)
- `memory/` – Sistema RAG e armazenamento
- `tools/` – Integrações externas
- `adapters/` – Interfaces com clientes e plataformas

## Instalação

```bash
pip install -r requirements.txt
```

## Execução de Exemplo

Para executar o orquestrador de exemplo:

```bash
python examples/run_orchestrator.py
```

O script carrega `system_config.yaml`, valida a configuração com `ConfigValidator` e inicia uma interação em linha de comando onde é possível digitar uma pergunta e receber a resposta do orquestrador.

## Testes

```bash
python -m pytest
```

## Documentação Auxiliar

- [Plano_de_arquitetura.md](Plano_de_arquitetura.md)
- [AI_AGENTS_GUIDE.md](AI_AGENTS_GUIDE.md)
