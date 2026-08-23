from scapy.all import sniff
from capture.packet_parser import PacketParser


class PacketCapture:
    def __init__(self, interface=None):
        self.interface = interface
        self.parser = PacketParser()

    def capture(self, count=10):
        print(f"Capturing {count} packets...")
        packets = sniff(iface=self.interface, count=count)
        print("Capture complete")
        return [self.parser.parse(packet) for packet in packets]