import json
import re

from src.utils.logger import get_logger


def test_get_logger_json_format(capsys):
    # Reset logger handlers because they are cached by name
    logger = get_logger("json_logger")
    logger.info("Hello, world!")

    captured = capsys.readouterr()
    log_data = json.loads(captured.out)

    assert log_data["levelname"] == "INFO"
    assert log_data["name"] == "json_logger"
    assert log_data["message"] == "Hello, world!"
    assert "asctime" in log_data


def test_get_logger_standard_format(capsys):
    # Use a different name to avoid using the same logger instance with existing handlers
    logger = get_logger("standard_logger", json_format=False)
    logger.info("Hello, standard!")

    captured = capsys.readouterr()
    pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] INFO standard_logger: Hello, standard!\n"
    assert re.match(pattern, captured.out)
