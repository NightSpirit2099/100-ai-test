# Agente Pessoal – Sistema Multi‑Agente

Este repositório implementa um **sistema multi‑agente de IA**. O Meta‑Orquestrador coordena agentes especializados com memória de longo prazo e estratégias de execução configuráveis. A configuração principal fica em `system_config.yaml`.

## Estrutura de diretórios

```
.
├── src/
│   ├── core/        # Meta‑Orquestrador e abstrações
│   ├── strategies/  # Estratégias de execução
│   ├── agents/      # Agentes especializados
│   ├── memory/      # Integração RAG
│   ├── tools/       # Integrações externas
│   └── adapters/    # Interfaces (Telegram, etc.)
├── tests/           # Testes unitários e de integração
├── system_config.yaml
├── validate_config.py
└── requirements.txt
```

## Instalação

```bash
pip install -r requirements.txt
```

## Validação básica

```bash
python validate_config.py system_config.yaml
pytest -v
```

## Documentos relacionados

- [Plano_de_arquitetura.md](Plano_de_arquitetura.md)
- [Plano_de_execucao.md](Plano_de_execucao.md)
- [AGENTS.md](AGENTS.md)
- [AI_AGENTS_GUIDE.md](AI_AGENTS_GUIDE.md)
- [TECH_DEBT_LOG.md](TECH_DEBT_LOG.md)

Esses arquivos contêm decisões de arquitetura, padrões de desenvolvimento e histórico de débito técnico.
