import logging
import sys
from typing import Optional

from pythonjsonlogger import jsonlogger


_default_handler = logging.StreamHandler(sys.stdout)
_default_formatter = jsonlogger.JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
_default_handler.setFormatter(_default_formatter)


def get_logger(name: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger instance with JSON formatting.
    Args:
        name (str, optional): Name of the logger. Defaults to None (root logger).
        level (int): Logging level. Defaults to logging.INFO.
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.addHandler(_default_handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger
