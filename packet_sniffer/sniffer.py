import logging
import time

from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logger.info("Starting packet sniffer")
    while True:
        time.sleep(1)
        raise ValueError("bad")
