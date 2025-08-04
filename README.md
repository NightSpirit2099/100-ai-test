# 100-ai-test

Projeto de exemplo para o sistema de Meta-Orquestração.

## Exemplo

Para executar o exemplo simples do orquestrador:

```bash
python examples/run_orchestrator.py
```

O script carrega `system_config.yaml`, valida a configuração com `ConfigValidator`
e inicia uma interação em linha de comando onde é possível digitar uma pergunta
e receber a resposta do orquestrador.

## Configuração do Sistema

Detalhes sobre o formato de `system_config.yaml` e como validá-lo estão descritos em [docs/system_config.md](docs/system_config.md).

## Modelo de Embeddings

`SimpleRAG` utiliza um modelo da biblioteca [`sentence-transformers`](https://www.sbert.net) para gerar embeddings de texto.
O modelo padrão é `"all-MiniLM-L6-v2"`. Na primeira execução, os pesos são baixados automaticamente.

Em ambientes sem acesso à internet, o download pode ser feito manualmente em outra máquina:

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2').save('./all-MiniLM-L6-v2')"
```

Depois, copie a pasta `all-MiniLM-L6-v2` para o ambiente restrito e defina a variável
`SENTENCE_TRANSFORMERS_HOME` apontando para esse diretório ou informe o caminho ao instanciar o `SentenceTransformer`.
