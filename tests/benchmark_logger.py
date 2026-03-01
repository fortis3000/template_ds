import logging
import os
import sys
import time

# Add src to sys.path to be able to import from it
sys.path.append(os.path.abspath("src"))

from utils.logger import get_logger


def benchmark(num_loggers=10000):
    start = time.perf_counter()
    for i in range(num_loggers):
        get_logger(f"logger_{i}")
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    # Measure time
    duration = benchmark()
    print(f"Time for 10000 loggers: {duration:.4f}s")

    # Measure number of handlers
    total_handlers = 0
    unique_handlers = set()
    for i in range(10000):
        logger = logging.getLogger(f"logger_{i}")
        total_handlers += len(logger.handlers)
        for h in logger.handlers:
            unique_handlers.add(id(h))

    print(f"Total handlers: {total_handlers}")
    print(f"Unique handlers: {len(unique_handlers)}")
