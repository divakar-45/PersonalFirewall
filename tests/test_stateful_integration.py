from core.connection_tracker import ConnectionTracker
from core.rule import FirewallRule
from core.rule_engine import RuleEngine
from core.traffic import Traffic


def tcp(direction, flags):
    if direction == "OUTBOUND":
        source_ip = "10.77.190.132"
        destination_ip = "142.250.1.1"
        source_port = 50000
        destination_port = 443
    else:
        source_ip = "142.250.1.1"
        destination_ip = "10.77.190.132"
        source_port = 443
        destination_port = 50000

    return Traffic(
        source_ip=source_ip,
        destination_ip=destination_ip,
        protocol="TCP",
        source_port=source_port,
        destination_port=destination_port,
        direction=direction,
        tcp_flags=flags
    )


def udp(direction):
    if direction == "OUTBOUND":
        source_ip = "10.77.190.132"
        destination_ip = "8.8.8.8"
        source_port = 53000
        destination_port = 53
    else:
        source_ip = "8.8.8.8"
        destination_ip = "10.77.190.132"
        source_port = 53
        destination_port = 53000

    return Traffic(
        source_ip=source_ip,
        destination_ip=destination_ip,
        protocol="UDP",
        source_port=source_port,
        destination_port=destination_port,
        direction=direction
    )


def process(tracker, engine, rules, packet):
    state = tracker.get_state(packet)
    flags = packet.tcp_flags or ""

    if packet.protocol == "TCP" and ("F" in flags or "R" in flags):
        if state is not None:
            decision = "ALLOW"
            state = tracker.update(packet)
        else:
            decision = engine.evaluate(rules, packet)

    elif state is not None:
        decision = "ALLOW"
        state = tracker.update(packet)

    else:
        decision = engine.evaluate(rules, packet)

        if decision == "ALLOW":
            state = tracker.update(packet)

    return state, decision


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

    tcp_packets = [
        tcp("OUTBOUND", "S"),
        tcp("INBOUND", "SA"),
        tcp("OUTBOUND", "A"),
        tcp("INBOUND", "PA"),
        tcp("OUTBOUND", "FA")
    ]

    print("TCP TEST")

    for packet in tcp_packets:
        state, decision = process(
            tracker,
            engine,
            rules,
            packet
        )

        print(
            packet.tcp_flags,
            "->",
            state or "NEW",
            "->",
            decision
        )

    print()
    print(
        "TCP CONNECTION EXISTS:",
        tracker.exists(tcp("OUTBOUND", "A"))
    )

    print()
    print("UDP TEST")

    udp_outbound = udp("OUTBOUND")
    udp_inbound = udp("INBOUND")

    state, decision = process(
        tracker,
        engine,
        rules,
        udp_outbound
    )

    print(
        "OUTBOUND ->",
        state or "NEW",
        "->",
        decision
    )

    state, decision = process(
        tracker,
        engine,
        rules,
        udp_inbound
    )

    print(
        "INBOUND ->",
        state or "NEW",
        "->",
        decision
    )


if __name__ == "__main__":
    main()