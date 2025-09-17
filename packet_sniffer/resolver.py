import logging
import random
import socket
import time

from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logger.info("Starting...")
    hostnames = ["google.com", "darktrace.com", "bbc.co.uk"]
    while True:
        time.sleep(1)
        hostname = random.choice(hostnames)
        resolved = socket.gethostbyname(hostname)
        logger.info("Resolved %s to %s", hostname, resolved)
