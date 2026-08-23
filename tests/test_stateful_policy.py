from core.connection_tracker import ConnectionTracker
from core.rule import FirewallRule
from core.rule_engine import RuleEngine
from core.traffic import Traffic


def main():
    tracker = ConnectionTracker()
    engine = RuleEngine()

    rules = [
        FirewallRule(
            action="ALLOW",
            priority=10,
            direction="OUTBOUND",
            protocol="TCP",
            destination_port=443
        ),
        FirewallRule(
            action="ALLOW",
            priority=20,
            direction="OUTBOUND",
            protocol="UDP",
            destination_port=53
        )
    ]

    tcp_outbound = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="S"
    )

    tcp_inbound = Traffic(
        source_ip="142.250.1.1",
        destination_ip="10.77.190.132",
        protocol="TCP",
        source_port=443,
        destination_port=50000,
        direction="INBOUND",
        tcp_flags="SA"
    )

    udp_outbound = Traffic(
        source_ip="10.77.190.132",
        destination_ip="8.8.8.8",
        protocol="UDP",
        source_port=53000,
        destination_port=53,
        direction="OUTBOUND"
    )

    blocked_udp = Traffic(
        source_ip="10.77.190.132",
        destination_ip="8.8.8.8",
        protocol="UDP",
        source_port=53001,
        destination_port=443,
        direction="OUTBOUND"
    )

    for traffic in [
        tcp_outbound,
        tcp_inbound,
        udp_outbound,
        blocked_udp
    ]:
        state = tracker.get_state(traffic)

        if state in ("ESTABLISHED", "ACTIVE"):
            decision = "ALLOW"
        else:
            decision = engine.evaluate(rules, traffic)

            if decision == "ALLOW":
                state = tracker.update(traffic)

        print(traffic)
        print("State:", state or "NEW")
        print("Decision:", decision)
        print()


if __name__ == "__main__":
    main()