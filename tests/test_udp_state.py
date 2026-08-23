from core.connection_tracker import ConnectionTracker
from core.traffic import Traffic


def main():
    tracker = ConnectionTracker(timeout=10)

    outbound = Traffic(
        source_ip="10.77.190.132",
        destination_ip="8.8.8.8",
        protocol="UDP",
        source_port=53000,
        destination_port=53,
        direction="OUTBOUND"
    )

    inbound = Traffic(
        source_ip="8.8.8.8",
        destination_ip="10.77.190.132",
        protocol="UDP",
        source_port=53,
        destination_port=53000,
        direction="INBOUND"
    )

    print("Before:", tracker.get_state(inbound))

    print("Outbound:", tracker.update(outbound))

    print("Inbound:", tracker.get_state(inbound))

    print("Allowed state:", tracker.is_established(inbound))


if __name__ == "__main__":
    main()