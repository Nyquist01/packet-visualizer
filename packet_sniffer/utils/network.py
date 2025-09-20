import ipaddress
import logging
import socket

logger = logging.getLogger()


def is_port_well_known(port: int) -> bool:
    """
    Checks whether the given port is in the well-known range 0 - 1023
    """
    return 0 <= port <= 1023


def resolve_ip_to_host(ip: str):
    try:
        if ipaddress.ip_address(ip).is_private:
            return None
    except ValueError:
        logger.error("Could not resolve IP: %s", ip)
        raise
    try:
        host = socket.gethostbyaddr(ip)
    except socket.herror:
        return None
    return host[0]
