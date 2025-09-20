import ipaddress
import logging
import socket
from multiprocessing import Queue

from .models import Packet, Connection
from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main(queue: Queue):
    setup_logging()
    logger.info("Starting...")
    while True:
        packet: Packet = queue.get()
        conn = Connection.from_packet(packet)
        conn.resolve_ips()
        logger.info(conn)
        