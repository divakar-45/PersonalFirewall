from scapy.layers.inet import IP, TCP

from capture.packet_parser import PacketParser
from core.rule import FirewallRule
from core.rule_engine import RuleEngine


def main():
    parser = PacketParser()
    engine = RuleEngine()

    rules = [
        FirewallRule(
            action="BLOCK",
            priority=10,
            direction="INBOUND",
            protocol="TCP",
            destination_port=22
        ),
        FirewallRule(
            action="ALLOW",
            priority=20,
            direction="INBOUND",
            protocol="TCP",
            destination_port=443
        )
    ]

    packets = [
        IP(
            src="8.8.8.8",
            dst="10.77.190.132"
        ) / TCP(
            sport=443,
            dport=22
        ),

        IP(
            src="8.8.8.8",
           dst="10.77.190.132"
        ) / TCP(
            sport=443,
            dport=443
        )
    ]

    for packet in packets:
        traffic = parser.parse(packet)
        decision = engine.evaluate(rules, traffic)

        print(traffic)
        print("Decision:", decision)
        print()


if __name__ == "__main__":
    main()