import logging
import sys
from typing import List, Optional

_HANDLERS: List[logging.Handler] = []


def get_logger(name: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger instance.
    Args:
        name (str, optional): Name of the logger. Defaults to None (root logger).
        level (int): Logging level. Defaults to logging.INFO.
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        if not _HANDLERS:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            _HANDLERS.append(handler)
        logger.addHandler(_HANDLERS[0])
    logger.setLevel(level)
    logger.propagate = False
    return logger
