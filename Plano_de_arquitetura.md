# Planta-Mestra Final: O Agente Pessoal (v3.0)

**ID do Documento:** `architectural_blueprint_final_v3.0.md`  
**Versão:** 3.0 (Final, Consolidada)  
**Status:** Aprovado para Execução Imediata  
**Data de Aprovação:** 02 de agosto de 2025

-----

## 1. Visão do Produto e Princípios Fundamentais

### 1.1. Visão
Construir um assistente pessoal que atua como uma **equipe de agentes de IA especialistas**. O sistema será proativo e reativo, com uma memória de longo prazo que o torna cada vez mais relevante com o tempo. A interação principal será via texto, começando com o Telegram.

### 1.2. Princípios Arquiteturais Chave
A arquitetura deste sistema é governada pelos seguintes princípios, acordados durante a fase de design:

* **Modularidade Extrema:** O sistema é projetado como um conjunto de componentes desacoplados, permitindo a evolução e substituição de partes sem impacto no todo.
* **Configuração sobre Código:** A lógica de negócio, a composição de equipes e as configurações de modelo são externalizadas para arquivos de configuração (`.yaml`), permitindo rápida iteração e flexibilidade.
* **NRAR (Não Reinvente a Roda):** Utilização massiva de frameworks e ferramentas de código aberto de alta qualidade (LangChain, CrewAI, Ollama, Neo4j) para focar o desenvolvimento na lógica de integração e no valor único do produto.
* **Execução Incremental:** A visão de longo prazo será alcançada através de um roadmap pragmático e faseado, começando com um MVP simples para validar as hipóteses centrais.
* **Organização de Código (Monorepo):** Todo o código residirá em um único repositório para simplificar a gestão de dependências e garantir a atomicidade das mudanças coordenadas.

## 2. Arquitetura de Alto Nível

A arquitetura é baseada em um **Meta-Orquestrador** que utiliza o **Padrão de Design Strategy** para selecionar o framework de execução apropriado para uma dada tarefa. Isso garante a flexibilidade para incorporar novos paradigmas de colaboração de agentes no futuro.

### 2.1. Diagrama Arquitetural Consolidado

```mermaid
graph TD
    subgraph "Fronteira Externa"
        User -- "Pedido" --> Adapter["Adaptador de Mensagens (Telegram)"];
    end

    subgraph "Núcleo do Sistema: O Orquestrador"
        Adapter -- "Input" --> MetaOrchestrator["Meta-Orquestrador"];
        MetaOrchestrator -- "1. Classifica e Seleciona Estratégia" --> IStrategy(Abstração: IExecutionStrategy);
        IStrategy -- "4. Retorna Resultado" --> MetaOrchestrator;
        MetaOrchestrator -- "Output" --> Adapter;
    end

    subgraph "Camada de Estratégias (Plugins)"
        CrewAIStrategy["Estratégia Concreta: CrewAI"] -- "Implementa" --> IStrategy;
        LangGraphStrategy["(Futuro) Estratégia: LangGraph"] -- "Implementa" --> IStrategy;
    end

    subgraph "Recursos da Equipe"
        CrewAIStrategy -- "2. Monta e Executa" --> Crew["Equipe de Agentes (Crew)"];
        Crew -- "3. Utiliza" --> Resources;
    end
    
    subgraph "Cérebro Híbrido"
         Resources -- "Raciocínio" --> Gemini["Cloud LLM (Gemini)"];
         Resources -- "Privacidade/Velocidade" --> Ollama["Local LLM (Ollama)"];
    end
    
    subgraph "Memória e Ferramentas"
        Resources -- "Gerencia" --> RAG["Memória Híbrida <br> (Graph-Vector RAG)"];
        Resources -- "Usa" --> Tools["Ferramentas <br> (Google, Web, etc.)"];
    end

3. Detalhamento dos Componentes Principais
 * Paradigma de Programação: Orientado a Objetos e a Componentes, utilizando classes Python para modelar as entidades do sistema.
 * Cérebro (LLM): Híbrido.
   * LLMs Locais (via Ollama): Para tarefas de alta privacidade, baixo custo e alta velocidade (ex: classificação de intenção, pré-processamento de dados do RAG).
   * LLM de Ponta (via Gemini API): Para tarefas de raciocínio complexo, planejamento e geração de conteúdo de alta qualidade.
 * Memória (RAG): Híbrida Grafo-Vetor.
   * Tecnologia: Banco de Dados de Grafo com suporte a índices vetoriais (Ex: Neo4j).
   * Mecanismo: O grafo armazena as relações estruturadas entre entidades, enquanto os nós do grafo contêm os embeddings vetoriais do conteúdo textual para busca semântica fina.
   * Agente Guardião: Um ArchivistAgent dedicado gerencia a pipeline de ingestão e recuperação da memória.
4. Roadmap de Execução Oficial (v2.0)
A implementação seguirá um plano de desenvolvimento incremental.
4.1. MVP (Fase 0): O Assistente de Conhecimento Mínimo
 * Objetivo: Validar o fluxo de ponta a ponta com a menor complexidade.
 * Componentes:
   * LLM: Single LLM (API do Gemini).
   * Memória: RAG Vetorial Simples (ChromaDB, baseado em arquivos).
   * Orquestração: Cadeia simples com LangChain LCEL.
   * Interface: Adaptador do Telegram.
 * Métricas de Sucesso: Setup Time < 15 min, First Response < 5s, RAG Accuracy > 70%.
4.2. Iteração 1: A Equipe de Especialistas
 * Objetivo: Introduzir a arquitetura multi-agente.
 * Ações: Refatorar a orquestração para usar CrewAI, introduzir os primeiros agentes especialistas e integrar a primeira ferramenta externa (Google Calendar).
4.3. Iteração 2: O Cérebro Híbrido
 * Objetivo: Implementar a estratégia de múltiplos LLMs.
 * Ações: Integrar o Ollama e implementar o "Roteador de LLM" baseado no system_config.yaml.
4.4. Iteração 3: A Memória Avançada
 * Objetivo: Evoluir para o sistema de memória de ponta.
 * Ações: Migrar o banco de dados para Neo4j, implementar a pipeline de ingestão para o Graph RAG e introduzir o LangGraph para orquestrar os fluxos de consulta complexos.
5. Governança e Práticas de Engenharia
 * system_config.yaml: Um arquivo de configuração central definirá agentes, tarefas, equipes e perfis de LLM, permitindo rápida iteração. Uma especificação detalhada e um validador (Pydantic) serão a primeira tarefa da Fase 0.
 * Gestão de Estado: A ingestão de dados para a memória salvará os dados brutos em formato JSONL, garantindo uma fonte da verdade agnóstica ao banco de dados para facilitar futuras migrações.
 * Gestão de Débito Técnico: Um TECH_DEBT_LOG.md será mantido no repositório para rastrear decisões e pontos de refatoração necessários.
 * Estratégia de Fallback: O sistema terá mecanismos de degradação graciosa para falhas em serviços externos (APIs, bancos de dados), informando o usuário sobre a limitação de capacidade.
 * Segurança e Privacidade: Chaves e tokens serão gerenciados via variáveis de ambiente (.env) e não serão commitados. O acesso à memória será auditado.
[FIM DO DOCUMENTO]
