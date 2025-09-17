import logging
import multiprocessing
import time

from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logger.info("Starting...")
    while True:
        time.sleep(1)
        logger.info("Sniffing")
