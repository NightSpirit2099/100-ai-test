# Agente Pessoal

Sistema multi-agente com orquestrador principal responsável por delegar solicitações para diferentes estratégias de execução.

## Registrando novas estratégias

1. Implemente a interface `IExecutionStrategy`:

```python
from src.core.interfaces import AgentResponse, IExecutionStrategy, UserRequest

class CustomStrategy:
    def execute(self, request: UserRequest) -> AgentResponse:
        return AgentResponse(text=f"Custom: {request.text}")
```

2. Registre a estratégia ao instanciar o `MetaOrchestrator`:

```python
from src.core.meta_orchestrator import MetaOrchestrator

strategies = {"custom": CustomStrategy()}
orch = MetaOrchestrator(strategies=strategies)
```

Após isso, a nova estratégia pode ser selecionada na análise ou chamada diretamente pelo identificador fornecido no dicionário.
