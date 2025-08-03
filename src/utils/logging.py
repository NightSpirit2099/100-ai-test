import logging
import sys
from typing import Optional

LOG_FORMAT = "%(levelname)s - %(name)s - %(message)s"

_configured = False

def configure_logging(level: int = logging.INFO) -> None:
    """Configure global logging once.

    Args:
        level: Minimum logging level.
    """
    global _configured
    if _configured:
        return

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(handler)

    _configured = True


def get_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """Return a logger configured with the global settings.

    Args:
        name: Logger name, typically ``__name__`` of the caller.
        level: Optional level override.
    """
    configure_logging(level if level is not None else logging.INFO)
    return logging.getLogger(name)
