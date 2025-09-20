import multiprocessing

import uvicorn

from .resolver import main as resolver_main
from .sniffer import main as sniffer_main


def main():
    packet_q = multiprocessing.Queue()

    sniffer_process = multiprocessing.Process(
        target=sniffer_main, args=[packet_q], name="sniffer"
    )
    resolver_process = multiprocessing.Process(
        target=resolver_main, args=[packet_q], name="resolver"
    )

    sniffer_process.start()
    resolver_process.start()
    uvicorn.run("packet_sniffer.server:app", host="0.0.0.0", port=8000, reload=True)
    sniffer_process.join()


if __name__ == "__main__":
    main()
