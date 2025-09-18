import ipaddress
import logging
import socket
from multiprocessing.connection import Connection as MultiprocessingConnection

from .models import Connection
from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main(queue: MultiprocessingConnection):
    setup_logging()
    logger.info("Starting...")
    while True:
        packet = queue.recv()
        # TODO: resolve the src and dst asynchronously
        if packet["src_ip"]:
            packet["src_host"] = get_host_from_ip(packet["src_ip"])
        if packet["dst_ip"]:
            packet["dst_host"] = get_host_from_ip(packet["dst_ip"])
        conn = Connection(**packet)
        logger.info(conn)


def get_host_from_ip(ip: str):
    if ipaddress.ip_address(ip).is_private:
        return None
    try:
        host = socket.gethostbyaddr(ip)
    except socket.herror:
        return None
    return host[0]
