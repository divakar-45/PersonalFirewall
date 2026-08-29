import json

from core.logger import FirewallLogger
from core.traffic import Traffic


def main():
    logger = FirewallLogger("logs/test_firewall.json.log")

    events = [
        Traffic(
            source_ip="10.77.190.132",
            destination_ip="8.8.8.8",
            protocol="TCP",
            source_port=50000,
            destination_port=443,
            direction="OUTBOUND",
            tcp_flags="S"
        ),
        Traffic(
            source_ip="10.77.190.132",
            destination_ip="8.8.8.8",
            protocol="UDP",
            source_port=53000,
            destination_port=53,
            direction="OUTBOUND"
        ),
        Traffic(
            source_ip="fe80::1",
            destination_ip="fe80::2",
            protocol="58",
            source_port=None,
            destination_port=None,
            direction="INBOUND"
        )
    ]

    for traffic in events:
        logger.log(
            traffic,
            "NEW",
            "BLOCK"
        )

    with open(
        "logs/test_firewall.json.log",
        "r",
        encoding="utf-8"
    ) as file:
        lines = file.readlines()

    if len(lines) != 3:
        raise AssertionError(
            f"Expected 3 log events, got {len(lines)}"
        )

    for line in lines:
        event = json.loads(line)

        required_fields = {
            "timestamp",
            "direction",
            "protocol",
            "source_ip",
            "source_port",
            "destination_ip",
            "destination_port",
            "state",
            "decision",
            "tcp_flags"
        }

        missing = required_fields - event.keys()

        if missing:
            raise AssertionError(
                f"Missing fields: {missing}"
            )

    print("JSON logger validation passed.")
    print("TCP, UDP, and portless protocol events are valid JSON.")


if __name__ == "__main__":
    main()