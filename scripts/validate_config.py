import logging
import sys
from pathlib import Path

import yaml
from pydantic import ValidationError

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def main(path: str) -> int:
    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.append(str(root))
    from config_models import SystemConfig
    from src.core.config_validator import ConfigValidator

    logger.info("Validando arquivo de configuração: %s", path)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error("Arquivo não encontrado: %s", path)
        return 1
    except yaml.YAMLError as e:
        logger.error("Erro ao ler YAML: %s", e)
        return 1

    try:
        config = SystemConfig.from_dict(data)
        ConfigValidator(config).validate()
    except ValidationError as e:
        for err in e.errors():
            if err.get("loc") == ("version",) and err.get("type") == "string_pattern_mismatch":
                logger.error(
                    "Versão inválida '%s': esperado formato 'X.Y'", err.get("input")
                )
                return 1
        logger.error("Configuração inválida: %s", e)
        return 1
    except Exception as e:  # pragma: no cover - salvaguarda
        logger.error("Falha inesperada na validação: %s", e)
        return 1

    logger.info("Configuração validada com sucesso.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error(
            "Uso: python scripts/validate_config.py <caminho_para_config.yaml>"
        )
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
