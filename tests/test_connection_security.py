from core.connection_tracker import ConnectionTracker
from core.traffic import Traffic


def create_traffic(flags):
    return Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags=flags
    )


def main():
    tracker = ConnectionTracker()

    syn = create_traffic("S")
    ack = create_traffic("A")

    tracker.update(syn)

    print("SYN established:", tracker.is_established(syn))

    tracker.update(ack)

    print("ACK established:", tracker.is_established(ack))


if __name__ == "__main__":
    main()