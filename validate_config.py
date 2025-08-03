import sys
import yaml
from pydantic import ValidationError

from config_models import SystemConfig


def main(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    try:
        SystemConfig.from_dict(data)
    except ValidationError as e:
        print("Config inválido:")
        print(e)
        return 1
    print("Config válido!")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python validate_config.py <caminho_para_config.yaml>")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
