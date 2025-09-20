import logging

from dataclasses import dataclass
from socket import getservbyport

from pyshark.packet.packet import Packet as PysharkPacket

from .utils.network import is_port_well_known, resolve_ip_to_host

logger = logging.getLogger()


class Packet:
    """Represents a packet's metadata as an object"""

    def __init__(self, packet: PysharkPacket):
        self._packet = packet
        self.src_ip = self.extract_src_ip()
        self.dst_ip = self.extract_dst_ip()
        self.src_port = self.extract_src_port()
        self.dst_port = self.extract_dst_port()

        self.src_port_name = None
        if self.src_port and is_port_well_known(self.src_port):
            try:
                self.src_port_name = getservbyport(self.src_port)
            except OSError as exc:
                logger.exception("Could not find proto for %s. Exception %s", self.src_port, exc)

        self.dst_port_name = None
        if self.dst_port and is_port_well_known(self.dst_port):
            try:
                self.dst_port_name = getservbyport(self.dst_port)
            except OSError:
                logger.exception("Could not find proto for %s. Exception %s", self.dst_port, exc)

    def to_dict(self) -> dict:
        return {
            "src_ip": self.src_ip,
            "dst_ip": self.dst_ip,
            "src_port": self.src_port,
            "dst_port": self.dst_port,
            "src_port_name": self.src_port_name,
            "dst_port_name": self.dst_port_name,
        }

    @property
    def _has_ip_layer(self):
        return bool("IP" in self._packet)

    @property
    def _has_tcp_layer(self):
        return bool("TCP" in self._packet)

    def extract_src_ip(self) -> str | None:
        if self._has_ip_layer:
            return str(self._packet.ip.src)
        return None

    def extract_dst_ip(self) -> str | None:
        if self._has_ip_layer:
            return str(self._packet.ip.dst)
        return None

    def extract_src_port(self) -> int | None:
        if self._has_tcp_layer:
            return int(self._packet.tcp.srcport)
        return None

    def extract_dst_port(self) -> int | None:
        if self._has_tcp_layer:
            return int(self._packet.tcp.dstport)
        return None
    
    def resolve_src_ip(self) -> None:
        self.src


@dataclass
class Connection:
    """Higher level representation of a packet"""

    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    src_port_name: str | None = None
    dst_port_name: str | None = None
    src_host: str | None = None
    dst_host: str | None = None
    src_host: str | None = None
    dst_host: str | None = None

    @classmethod
    def from_packet(cls, packet: Packet) -> "Connection":
        return cls(
            src_ip=packet.src_ip,
            dst_ip=packet.dst_ip,
            src_port=packet.src_port,
            dst_port=packet.dst_port,
            src_port_name=packet.src_port_name,
            dst_port_name=packet.dst_port_name
        )
    
    def resolve_ips(self):
        # TODO: resolve the hosts asynchronously
        if self.src_ip:
            self.src_host = resolve_ip_to_host(self.src_ip)
        if self.dst_ip:
            self.dst_host = resolve_ip_to_host(self.dst_ip)

    def __str__(self):
        src = self.src_host or self.src_ip
        dst = self.dst_host or self.dst_ip
        sport = self.src_port_name or self.src_port
        dport = self.dst_port_name or self.dst_port
        return f"src={src}:{sport}   ----->   dst={dst}:{dport}"
