import multiprocessing

from .resolver import main as resolver_main
from .sniffer import main as sniffer_main


def main():
    queue = multiprocessing.Queue()
    resolver_process = multiprocessing.Process(
        target=resolver_main, args=[queue], name="resolver"
    )
    sniffer_process = multiprocessing.Process(
        target=sniffer_main, args=[queue], name="sniffer"
    )

    resolver_process.start()
    sniffer_process.start()
    sniffer_process.join()


if __name__ == "__main__":
    main()
