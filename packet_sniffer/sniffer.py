import logging
from multiprocessing.connection import Connection

import pyshark

from .models import Packet
from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main(queue: Connection):
    setup_logging()
    logger.info("Starting")
    cap = pyshark.LiveRingCapture()
    for packet in cap.sniff_continuously():
        packet = Packet(packet)
        queue.send(packet.to_dict())
