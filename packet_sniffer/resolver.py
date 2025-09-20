import logging
from multiprocessing import Queue

from .consts import REDIS_QUEUE_KEY
from .models import Connection, Packet
from .redis_client import ConnectionQueue, redis_client
from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main(mp_queue: Queue):
    setup_logging()
    logger.info("Starting...")
    redis = redis_client()
    rd_queue = ConnectionQueue(redis, REDIS_QUEUE_KEY)

    while True:
        packet: Packet = mp_queue.get()
        conn = Connection.from_packet(packet)
        conn.resolve_ips()
        rd_queue.push(conn.to_json())
