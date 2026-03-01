import io
import os
import sys

# Add src to sys.path
sys.path.append(os.path.abspath("src"))

from utils.logger import get_logger


def test_logger_shared_handler():
    logger_a = get_logger("LoggerA")
    logger_b = get_logger("LoggerB")

    # Verify they share the same handler
    assert logger_a.handlers[0] is logger_b.handlers[0]

    # Verify unique names in logs
    # Capture stdout
    stdout_capture = io.StringIO()
    # We need to temporarily replace the stream in the shared handler
    shared_handler = logger_a.handlers[0]
    original_stream = shared_handler.stream
    shared_handler.stream = stdout_capture

    try:
        logger_a.info("Message from A")
        logger_b.info("Message from B")

        output = stdout_capture.getvalue()
        print(output)

        assert "INFO LoggerA: Message from A" in output
        assert "INFO LoggerB: Message from B" in output
    finally:
        shared_handler.stream = original_stream


if __name__ == "__main__":
    try:
        test_logger_shared_handler()
        print("Functional test passed!")
    except Exception as e:
        print(f"Functional test failed: {e}")
        sys.exit(1)
