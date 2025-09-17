import logging
import multiprocessing

from packet_sniffer.parser import main as parser
from packet_sniffer.resolver import main as resolver
from packet_sniffer.sniffer import main as sniffer

logger = logging.getLogger(__name__)


def main():
    parser_process = multiprocessing.Process(target=parser)
    resolver_process = multiprocessing.Process(target=resolver)
    sniffer_process = multiprocessing.Process(target=sniffer)

    parser_process.start()
    resolver_process.start()
    sniffer_process.start()


if __name__ == "__main__":
    main()
