import pytest  # noqa: F401
from src.utils import logger


def test_logger_basic_usage(caplog):
    log = logger.get_logger("test")
    with caplog.at_level("INFO"):
        log.info("Logger works!")
    assert log.name == "test"
    assert any("Logger works!" in message for message in caplog.messages)
