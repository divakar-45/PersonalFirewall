from core.connection_tracker import ConnectionTracker
from core.traffic import Traffic


def main():
    tracker = ConnectionTracker()

    outbound = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=54567,
        destination_port=443,
        direction="OUTBOUND"
    )

    inbound = Traffic(
        source_ip="142.250.1.1",
        destination_ip="10.77.190.132",
        protocol="TCP",
        source_port=443,
        destination_port=54567,
        direction="INBOUND"
    )

    print("Before tracking:", tracker.exists(inbound))

    tracker.add(outbound)

    print("After tracking:", tracker.exists(inbound))


if __name__ == "__main__":
    main()