from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6
from capture.packet_parser import PacketParser


def main():
    parser = PacketParser()

    packets = [
        IP(src="192.168.1.10", dst="8.8.8.8") / TCP(
            sport=50000,
            dport=443
        ),
        IP(src="192.168.1.10", dst="8.8.8.8") / UDP(
            sport=53000,
            dport=53
        ),
        IP(src="192.168.1.10", dst="8.8.8.8") / ICMP(),
        IPv6(src="2001:db8::10", dst="2001:db8::20") / TCP(
            sport=50000,
            dport=443
        ),
        IPv6(src="2001:db8::10", dst="2001:db8::20") / UDP(
            sport=53000,
            dport=53
        )
    ]

    for packet in packets:
        print(parser.parse(packet))


if __name__ == "__main__":
    main()