import logging
import sys

import yaml
from pydantic import ValidationError

from config_models import SystemConfig
from src.core.config_validator import ConfigValidator

logger = logging.getLogger(__name__)


def main(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    try:
        config = SystemConfig.from_dict(data)
        ConfigValidator(config).validate()
    except ValidationError as e:
        logger.error("Config inválido: %s", e)
        return 1
    logger.info("Config válido!")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Uso: python validate_config.py <caminho_para_config.yaml>")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
