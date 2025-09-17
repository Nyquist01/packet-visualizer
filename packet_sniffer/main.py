from scapy.all import sniff


def print_packet(pkt):
    print(pkt.summary())


def main():
    sniff(prn=print_packet)


if __name__ == "__main__":
    main()
