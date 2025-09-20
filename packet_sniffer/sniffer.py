import logging
from multiprocessing import Queue

import pyshark

from .consts import BFP
from .models import Packet
from .utils.logger import setup_logging

logger = logging.getLogger(__name__)


def main(queue: Queue):
    setup_logging()
    logger.info("Starting")
    cap = pyshark.LiveCapture(bpf_filter=BFP)
    for packet in cap.sniff_continuously():
        packet = Packet(packet)
        queue.put(packet)
