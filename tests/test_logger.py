import pytest
from src.utils import logger

def test_logger_basic_usage():
    log = logger.get_logger("test")
    assert log.name == "test"
    log.info("Logger works!")
