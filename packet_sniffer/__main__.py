import multiprocessing

from packet_sniffer.resolver import main as resolver_main
from packet_sniffer.sniffer import main as sniffer_main


def main():
    consumer, producer = multiprocessing.Pipe()
    resolver_process = multiprocessing.Process(
        target=resolver_main, args=[consumer], name="resolver"
    )
    sniffer_process = multiprocessing.Process(
        target=sniffer_main, args=[producer], name="sniffer"
    )

    resolver_process.start()
    sniffer_process.start()


if __name__ == "__main__":
    main()
