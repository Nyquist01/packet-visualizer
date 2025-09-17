"""
Extracts metadata from packets
"""


import logging
import time

from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logger.info("Starting...")
    while True:
        time.sleep(0.5)
        logger.info("Parsing")
