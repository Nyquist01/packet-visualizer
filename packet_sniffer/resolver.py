import logging
import socket
import time

from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logging.info("Starting DNS resolver")
    while True:
        time.sleep(1)
        resolved = socket.gethostbyname("darktrace.com")
        print(resolved)
