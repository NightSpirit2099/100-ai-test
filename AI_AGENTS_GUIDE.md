# AI_AGENTS_GUIDE.md

## Propósito

Guia para agentes de IA que contribuirão com o desenvolvimento do **Agente Pessoal**. Este arquivo fornece contexto, estado atual e diretrizes para colaboração efetiva.

-----

## 🎯 CONTEXTO DO PROJETO

### O Que Estamos Construindo

Um assistente pessoal baseado em IA que atua como uma equipe de agentes especializados, com memória de longo prazo e capacidade proativa/reativa.

### Arquitetura Central

- **Meta-Orquestrador**: Núcleo que seleciona estratégias de execução
- **Padrão Strategy**: Permite múltiplos frameworks de orquestração
- **RAG Híbrido**: Memória de longo prazo (ChromaDB → Neo4j)
- **LLMs Híbridos**: Local (Ollama) + Nuvem (Gemini)
- **Interface**: Telegram (inicial)

### Roadmap Incremental

1. **MVP**: LLM + RAG simples + Telegram
1. **Iteração 1**: Multi-agentes com CrewAI
1. **Iteração 2**: LLMs híbridos
1. **Iteração 3**: RAG Graph-Vector avançado

-----

## 📊 ESTADO ATUAL DO PROJETO

### ✅ Implementado

```
[Atualizar conforme progresso]

Estrutura Base:
- src/core/ - Meta-Orquestrador (esqueleto)
- src/strategies/ - Interface IExecutionStrategy
- system_config.yaml - Template de configuração
- requirements.txt - Dependências base
- CI/CD pipeline - Validação automática
```

### 🔄 Em Desenvolvimento

```
[Atualizar diariamente]

Meta-Orquestrador Core:
- Status: 60% completo
- Arquivo: src/core/meta_orchestrator.py
- Pendente: analyze_request() e select_strategy()

ChromaDB Integration:
- Status: 30% completo  
- Arquivo: src/memory/simple_rag.py
- Pendente: Pipeline de ingestão
```

### ⏳ Próximo na Fila

```
[Prioridade ordenada]

1. Telegram Adapter (src/adapters/telegram_adapter.py)
2. ArchivistAgent MVP (src/agents/archivist_agent.py)
3. CrewAI Strategy (src/strategies/crewai_strategy.py)
4. System Config Validator (src/core/config_validator.py)
```

-----

## 🤖 DIRETRIZES PARA AGENTES DE IA

### Antes de Implementar

1. **Leia o contexto completo** - Entenda a arquitetura e decisões já tomadas
1. **Verifique dependências** - Confirme que componentes necessários existem
1. **Consulte configurações** - Sempre referencie `system_config.yaml`
1. **Revise padrões** - Siga diretrizes do `AGENTS.md`

### Durante a Implementação

1. **Mantenha consistência** - Use padrões já estabelecidos
1. **Documente decisões** - Atualize `TECH_DEBT_LOG.md` se necessário
1. **Implemente incrementalmente** - Foque na funcionalidade mínima viável
1. **Teste conforme desenvolve** - Inclua testes unitários básicos

### Após Implementar

1. **Atualize este arquivo** - Mova item de “Próximo” para “Implementado”
1. **Documente APIs** - Adicione docstrings e exemplos de uso
1. **Valide integração** - Confirme que funciona com componentes existentes
1. **Registre débito técnico** - Anote melhorias futuras necessárias

-----

## 📁 ESTRUTURA E CONVENÇÕES

### Estrutura de Diretórios

```
src/
├── core/           # Meta-Orquestrador, interfaces base
├── strategies/     # Implementações de IExecutionStrategy
├── agents/         # Agentes especializados (Archivist, etc.)
├── memory/         # Sistema RAG e persistência
├── tools/          # Integrações externas (Google, Web)
├── adapters/       # Interfaces de entrada (Telegram, etc.)
└── utils/          # Utilitários compartilhados
```

### Padrões de Naming

```python
# Classes: PascalCase
class MetaOrchestrator:
class ArchivistAgent:

# Arquivos: snake_case
meta_orchestrator.py
telegram_adapter.py

# Métodos: snake_case
def analyze_request():
def execute_strategy():

# Constantes: UPPER_CASE
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30
```

### Imports e Dependências

```python
# Sempre use imports absolutos
from src.core.interfaces import IExecutionStrategy
from src.memory.simple_rag import SimpleRAG

# Evite imports circulares
# Use typing.TYPE_CHECKING se necessário

# Dependências externas no topo
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Dependências internas após
from src.core.models import UserRequest, AgentResponse
```

-----

## 🔧 COMPONENTES CRÍTICOS

### Meta-Orquestrador

```python
# Localização: src/core/meta_orchestrator.py
# Status: Interface definida, implementação 60%
# Próximo: Completar analyze_request() e strategy selection

class MetaOrchestrator:
    def analyze_request(self, request: UserRequest) -> RequestAnalysis:
        # TODO: Implementar análise de intenção
        pass
    
    def select_strategy(self, analysis: RequestAnalysis) -> IExecutionStrategy:
        # TODO: Lógica de seleção de estratégia
        pass
```

### System Config

```yaml
# Localização: system_config.yaml
# Status: Template básico criado
# Próximo: Adicionar validação com Pydantic

version: "1.0"
llm:
  primary:
    provider: "gemini"
    model: "gemini-pro"
memory:
  type: "vector"
  provider: "chromadb"
agents:
  archivist:
    role: "Knowledge Retriever"
```

### Modelos de Dados

```python
# Localização: src/core/models.py
# Status: Definições básicas existem
# Próximo: Validar com casos de uso reais

class UserRequest(BaseModel):
    text: str
    context: Dict = {}
    timestamp: datetime = Field(default_factory=datetime.now)

class AgentResponse(BaseModel):
    content: str
    metadata: Dict = {}
    agent_id: str
```

-----

## 🚨 PONTOS DE ATENÇÃO

### Decisões Arquiteturais Fixas

- **Não altere**: Padrão Strategy do Meta-Orquestrador
- **Não altere**: Estrutura de diretórios estabelecida
- **Não altere**: Convenções de configuração YAML

### Áreas de Flexibilidade

- **Implementação interna** dos agentes (desde que sigam interfaces)
- **Otimizações de performance** (desde que mantenham compatibilidade)
- **Adição de utilidades** em `src/utils/`

### Débito Técnico Conhecido

```
[Consulte TECH_DEBT_LOG.md para lista completa]

1. ChromaDB ainda não tem pipeline de ingestão completa
2. Validação de system_config.yaml não implementada
3. Logging infrastructure básica pendente
4. Testes de integração end-to-end faltando
```

-----

## 🎯 CASOS DE USO PRIORITÁRIOS

### MVP - Funcionalidade Mínima

```
Usuário: "O que discutimos na reunião de ontem?"
Sistema: 
1. Meta-Orquestrador analisa pedido
2. Seleciona SimpleRAG strategy
3. ArchivistAgent busca na memória
4. Retorna resposta via Telegram
```

### Iteração 1 - Multi-Agentes

```
Usuário: "Prepare um resumo da reunião e envie por email"
Sistema:
1. Meta-Orquestrador seleciona CrewAI strategy
2. ArchivistAgent recupera dados da reunião
3. CommunicatorAgent drafta email
4. Confirma com usuário antes de enviar
```

-----

## 📝 TEMPLATES PARA IMPLEMENTAÇÃO

### Template para Novo Agente

```python
from src.core.interfaces import IAgent
from src.core.models import AgentRequest, AgentResponse

class NovoAgent(IAgent):
    """
    Descrição: [Responsabilidade do agente]
    Capabilities: [Lista de capacidades]
    Dependencies: [Dependências de outros componentes]
    """
    
    def __init__(self, config: Dict):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def execute(self, request: AgentRequest) -> AgentResponse:
        """Implementação da lógica principal"""
        self.logger.info(f"Executing {self.__class__.__name__}")
        
        # Implementação aqui
        
        return AgentResponse(
            content="Resultado da execução",
            metadata={"agent": self.__class__.__name__}
        )
```

### Template para Nova Strategy

```python
from src.core.interfaces import IExecutionStrategy
from src.core.models import UserRequest, AgentResponse

class NovaStrategy(IExecutionStrategy):
    """
    Strategy para: [Tipo de execução]
    Use cases: [Casos de uso específicos]
    Framework: [Framework utilizado, se aplicável]
    """
    
    def execute(self, request: UserRequest) -> AgentResponse:
        """Implementa lógica de orquestração específica"""
        
        # Lógica de orquestração aqui
        
        return AgentResponse(content="Resultado")
```

-----

## 🔄 PROCESSO DE ATUALIZAÇÃO

### Responsabilidade dos Agentes de IA

1. **Sempre atualize** a seção “Estado Atual” ao completar implementações
1. **Mova itens** de “Próximo na Fila” para “Em Desenvolvimento” ao iniciar
1. **Documente decisões** importantes tomadas durante implementação
1. **Registre débito técnico** identificado durante desenvolvimento

### Formato de Atualização

```markdown
### [Data] Implementado: [Nome do Componente]
**Arquivo**: caminho/do/arquivo.py
**Funcionalidade**: Descrição breve do que foi implementado
**Testes**: Status dos testes (✅ Completo / ⏳ Básico / ❌ Pendente)
**Débito Técnico**: Lista de melhorias futuras identificadas
**Próximas Dependências**: O que este componente desbloqueia
```

-----

## 📚 RECURSOS DE REFERÊNCIA

### Documentação Essencial

- `Plano_de_arquitetura.md` - Visão completa da arquitetura
- `Plano_de_execucao.md` - Roadmap e métricas
- `AGENTS.md` - Padrões de código e processo
- `TECH_DEBT_LOG.md` - Registro de melhorias futuras

### Configurações

- `system_config.yaml` - Configuração central do sistema
- `requirements.txt` - Dependências Python
- `.env.example` - Template para variáveis de ambiente

### Scripts Úteis

- `scripts/validate_config.py` - Validação de configuração
- `scripts/run_tests.py` - Execução de testes
- `scripts/setup_dev.py` - Setup do ambiente de desenvolvimento

-----

**Última Atualização**: [Manter sempre atual]  
**Próxima Revisão**: [Após cada implementação significativa]

-----

## 💡 DICAS PARA AGENTES DE IA

### Para Máxima Efetividade

1. **Leia tudo primeiro** - Este arquivo, arquitetura, e código existente
1. **Mantenha consistência** - Siga padrões já estabelecidos religiosamente
1. **Implemente incrementalmente** - Funcionalidade mínima primeiro
1. **Documente tudo** - Futuras iterações dependerão disso
1. **Teste conforme desenvolve** - Quebrar o MVP não é uma opção

### Quando em Dúvida

1. Consulte `Plano_de_arquitetura.md` para decisões de design
1. Verifique `AGENTS.md` para padrões de código
1. Examine código existente para consistência
1. Implemente a versão mais simples que funciona
1. Documente a decisão para revisão futura
