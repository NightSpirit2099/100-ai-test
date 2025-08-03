# Plano de Execução do Projeto: O Agente Pessoal

## 1. Contexto
O projeto visa construir um assistente pessoal composto por uma equipe de agentes de IA especialistas com memória de longo prazo e interação via texto pelo Telegram.

## 2. Escopo e Princípios
- Modularidade extrema
- Configuração sobre código
- NRAR (Não Reinvente a Roda)
- Execução incremental
- Organização de código em monorepo

## 3. Roadmap e Entregáveis
### Fase 0 - MVP (Assistente de Conhecimento Mínimo)
- Objetivo: Validar o fluxo de ponta a ponta com a menor complexidade.
- Entregáveis: LLM via Gemini, RAG vetorial simples (ChromaDB), orquestração com LangChain LCEL e adaptador Telegram.
- Métricas de sucesso: Setup < 15 min, First Response < 5s, RAG Accuracy > 70%.

### Iteração 1 - Equipe de Especialistas
- Objetivo: Introduzir a arquitetura multi-agente.
- Ações: Refatorar a orquestração para usar CrewAI, adicionar agentes especialistas e integrar o Google Calendar.

### Iteração 2 - Cérebro Híbrido
- Objetivo: Implementar a estratégia de múltiplos LLMs.
- Ações: Integrar o Ollama e implementar o roteador de LLM baseado no system_config.yaml.

### Iteração 3 - Memória Avançada
- Objetivo: Evoluir para o sistema de memória de ponta.
- Ações: Migrar o banco de dados para Neo4j, implementar a pipeline de ingestão para Graph RAG e introduzir o LangGraph.

## 4. Governança e Engenharia
- Criar system_config.yaml para definir agentes, tarefas, equipes e perfis de LLM.
- Gerenciar estado: salvar dados brutos em JSONL para facilitar migrações.
- Manter TECH_DEBT_LOG.md para rastrear decisões e refatorações.
- Implementar estratégia de fallback para serviços externos.
- Proteger chaves e tokens via variáveis de ambiente (.env) e auditar acesso à memória.

## 5. Plano de Execução Resumido
1. Semana 1: Especificação e validador do system_config.yaml.
2. Semana 2: Implementação do MVP (LLM, RAG, orquestração, adaptador Telegram).
3. Semana 3: Testes do MVP e validação das métricas.
4. Semana 4: Iteração 1 (CrewAI, agentes especialistas, Google Calendar).
5. Semana 5: Iteração 2 (Ollama, roteador de LLM).
6. Semana 6: Iteração 3 (Neo4j, pipeline Graph RAG, LangGraph).

## 6. Riscos e Mitigações
- Dependência de serviços externos: usar fallback e monitorar falhas.
- Complexidade da memória híbrida: implementar de forma incremental e validar cada etapa.
- Privacidade e segurança: gestão de tokens em .env e auditoria do acesso à memória.

## 7. Documentação e Seguimento
- Registrar decisões técnicas em TECH_DEBT_LOG.md.
- Atualizar a documentação ao final de cada fase.
- Realizar revisões semanais de progresso com a equipe.
