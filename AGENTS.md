# AGENTS.md

## Escopo e Propósito

Diretrizes técnicas e de processo para desenvolvedores contribuindo no **Agente Pessoal** - um sistema multi-agente de IA com arquitetura híbrida e memória de longo prazo.

Este documento define padrões que garantem:

- Consistência com a arquitetura Meta-Orquestrador estabelecida
- Qualidade e maintibilidade do código
- Processo de desenvolvimento iterativo e validado

## Estrutura do Projeto

### Documentos Arquiteturais Principais

- `Plano_de_arquitetura.md` - Planta-mestra e decisões técnicas
- `Plano_de_execucao.md` - Roadmap incremental e métricas
- `TECH_DEBT_LOG.md` - Registro de refatorações e decisões temporárias
- `system_config.yaml` - Configuração central do sistema

### Hierarquia de Módulos

```
src/
├── core/           # Meta-Orquestrador e abstrações
├── strategies/     # Implementações de IExecutionStrategy  
├── agents/         # Agentes especializados (ArchivistAgent, etc.)
├── memory/         # Sistema RAG (ChromaDB → Neo4j)
├── tools/          # Integrações externas
└── adapters/       # Interfaces (Telegram, etc.)
```

## Padrões de Código

### Python e Tipagem

- **Versão**: Python 3.10+
- **Estilo**: PEP 8 rigorosamente aplicado
- **Tipagem**: Obrigatória para todas as funções públicas
- **Validação**: Pydantic para modelos de dados

### Interfaces e Abstrações

```python
# Use typing.Protocol para definir contratos
from typing import Protocol

class IExecutionStrategy(Protocol):
    def execute(self, request: UserRequest) -> AgentResponse:
        ...

# Implementações devem seguir o padrão
class CrewAIStrategy:
    def execute(self, request: UserRequest) -> AgentResponse:
        # Implementação concreta
        pass
```

### Modelos Pydantic

```python
from pydantic import BaseModel, Field

class AgentConfig(BaseModel):
    name: str = Field(..., description="Nome único do agente")
    role: str = Field(..., description="Responsabilidade principal")
    max_iterations: int = Field(5, description="Limite de iterações")
    
    class Config:
        extra = "forbid"  # Previne campos não declarados
```

### Logging e Observabilidade

```python
import logging
from functools import wraps

# Logger centralizado por módulo
logger = logging.getLogger(__name__)

# Decorator para auditoria de agentes
def audit_agent_action(action_type: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Agent action: {action_type} started")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Agent action: {action_type} completed")
                return result
            except Exception as e:
                logger.error(f"Agent action: {action_type} failed: {e}")
                raise
        return wrapper
    return decorator
```

## Configuração e Validação

### Arquivo system_config.yaml

- **Localização**: Raiz do projeto
- **Validação**: Obrigatória via `ConfigValidator` antes de uso
- **Versionamento**: Incluir campo `version` em mudanças significativas

### Processo de Validação

```bash
# Antes de qualquer commit
python scripts/validate_config.py system_config.yaml
python scripts/validate_interfaces.py
python -m pytest tests/ -v
```

### Gestão de Segredos

```bash
# .env (NUNCA versionar)
GEMINI_API_KEY=your_key_here
TELEGRAM_BOT_TOKEN=your_token_here

# Carregamento no código
from dotenv import load_dotenv
load_dotenv()
```

## Fluxo de Desenvolvimento

### Processo de Contribuição

1. **Branch Strategy**: Feature branches a partir de `develop`
1. **Commits**: Pequenos, atômicos e descritivos
1. **Code Review**: Obrigatório para mudanças em `core/` e `strategies/`
1. **Testes**: Cobertura mínima de 80% para novos módulos

### Pipeline de CI/CD

```yaml
# Verificações obrigatórias
- Análise estática (mypy, pylint)
- Testes unitários e de integração
- Validação de configuração
- Verificação de complexidade ciclomática (< 10)
- Audit de segurança (bandit)
```

### Métricas de Qualidade

- **Latência de Resposta**: < 5s (monitorado via logs)
- **Cobertura de Testes**: > 80%
- **Complexidade Ciclomática**: < 10 por função
- **Conformidade PEP 8**: 100%

## Gestão de Débito Técnico

### TECH_DEBT_LOG.md

Registro obrigatório para:

- Abstrações temporárias que virarão interfaces
- Hardcodes que serão migrados para configuração
- TODOs com prazo de resolução
- Decisões de design que precisam revisão

Formato:

```markdown
## [2025-08-03] Abstração Temporária - ChromaDB Direct Access
**Localização**: `src/memory/simple_rag.py:45`
**Descrição**: Acesso direto ao ChromaDB sem interface
**Refatoração Planejada**: Iteração 3 (migração para Neo4j)
**Responsável**: @arquiteto_principal
```

## Padrões de Teste

### Estrutura de Testes

```
tests/
├── unit/           # Testes isolados por módulo
├── integration/    # Testes de fluxo end-to-end
├── fixtures/       # Dados de teste e mocks
└── performance/    # Testes de latência e throughput
```

### Testes de Contrato

```python
# Teste para verificar implementação de interfaces
def test_crewai_strategy_implements_interface():
    strategy = CrewAIStrategy()
    assert isinstance(strategy, IExecutionStrategy)
    
    # Teste de contrato
    request = UserRequest(text="test")
    response = strategy.execute(request)
    assert isinstance(response, AgentResponse)
```

## Monitoramento e Observabilidade

### Métricas Obrigatórias

- Tempo de resposta por endpoint
- Taxa de sucesso/falha de agentes
- Utilização de memória (RAG)
- Latência de LLM (local vs nuvem)

### Auditoria de Segurança

- Log de todas as consultas à memória
- Sanitização de inputs do usuário
- Rotação de tokens/chaves

## Definição de Pronto (DoD)

Uma feature está pronta quando:

- [ ] Código segue todos os padrões definidos
- [ ] Testes passam com cobertura > 80%
- [ ] Configuração validada via `validate_config.py`
- [ ] Documentação atualizada (se aplicável)
- [ ] TECH_DEBT_LOG.md atualizado
- [ ] Code review aprovado
- [ ] Métricas de performance dentro dos limites

## Contatos e Responsabilidades

- **Arquiteto Principal**: Decisões de design e refatorações críticas
- **Tech Lead**: Code review e padrões de código
- **DevOps**: Pipeline CI/CD e monitoramento
- **QA**: Definição e validação de métricas

-----

**Versão**: 2.0  
**Última Atualização**: 2025-08-03  
**Próxima Revisão**: Pós-MVP (conforme cronograma estabelecido)
