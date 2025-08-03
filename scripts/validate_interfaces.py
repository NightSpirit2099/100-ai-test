import importlib
import inspect
import logging
import pkgutil
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.interfaces import IExecutionStrategy

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def _iter_strategy_modules():
    package_dir = Path(__file__).resolve().parent.parent / "src" / "strategies"
    for module_info in pkgutil.iter_modules([str(package_dir)]):
        if module_info.name.startswith("_"):
            continue
        module_name = f"src.strategies.{module_info.name}"
        yield importlib.import_module(module_name)


def _is_concrete(cls: type) -> bool:
    return not bool(getattr(cls, "__abstractmethods__", False))


def main() -> int:
    expected_sig = inspect.signature(IExecutionStrategy.execute)
    try:
        for module in _iter_strategy_modules():
            logger.info("Verificando módulo: %s", module.__name__)
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__ != module.__name__:
                    continue
                if not _is_concrete(obj):
                    continue
                if not hasattr(obj, "execute"):
                    raise TypeError(
                        f"{obj.__name__} não implementa método 'execute'"
                    )
                sig = inspect.signature(obj.execute)
                if (
                    sig.parameters.keys() != expected_sig.parameters.keys()
                    or sig.return_annotation != expected_sig.return_annotation
                ):
                    raise TypeError(
                        f"{obj.__name__} não segue o contrato de IExecutionStrategy"
                    )
    except Exception as e:  # pragma: no cover - salvaguarda
        logger.error("Validação de interfaces falhou: %s", e)
        return 1
    logger.info("Todas as estratégias implementam IExecutionStrategy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
