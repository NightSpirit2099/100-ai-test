# System Configuration

The `system_config.yaml` file defines how the orchestrator runs. The main fields are:

- **`version`**: Semantic version of the configuration schema.
- **`llm_profiles`**: Named Large Language Model profiles with provider, model, and optional parameters such as temperature.
- **`agents`**: Definitions of specialized agents and which LLM profile each uses.
- **`tasks`**: Available tasks and the agent responsible for each task.
- **`teams`**: Groups of agents that can collaborate to accomplish tasks.

## Example

```yaml
version: "1.0"
llm_profiles:
  default:
    provider: gemini
    model: gemini-pro
    temperature: 0.7
agents:
  researcher:
    description: "General knowledge assistant"
    llm: default
tasks:
  answer_question:
    description: "Answer user questions"
    agent: researcher
teams:
  default:
    agents:
      - researcher
```

## Validation

To validate a configuration file before use, run:

```bash
python scripts/validate_config.py system_config.yaml
```

This command checks the file against the Pydantic models and custom rules.

