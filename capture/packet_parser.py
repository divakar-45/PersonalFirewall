from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.inet6 import IPv6
from core.network import get_local_addresses
from core.traffic import Traffic


class PacketParser:
    def parse(self, packet):
        if packet.haslayer(IP):
            network = packet[IP]
        elif packet.haslayer(IPv6):
            network = packet[IPv6]
        else:
            return None

        local_addresses = get_local_addresses()

        if network.src in local_addresses:
            direction = "OUTBOUND"
        elif network.dst in local_addresses:
            direction = "INBOUND"
        else:
            direction = "UNKNOWN"

        source_port = None
        destination_port = None

        if packet.haslayer(TCP):
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport
        else:
            protocol = str(network.nh if packet.haslayer(IPv6) else network.proto)

        return Traffic(
            source_ip=network.src,
            destination_ip=network.dst,
            protocol=protocol,
            source_port=source_port,
            destination_port=destination_port,
            direction=direction
        )