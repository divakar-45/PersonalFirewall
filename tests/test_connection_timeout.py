import time

from core.connection_tracker import ConnectionTracker
from core.traffic import Traffic


def main():
    tracker = ConnectionTracker(timeout=1)

    traffic = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="A"
    )

    tracker.update(traffic)

    print("Immediately:", tracker.exists(traffic))

    time.sleep(2)

    print("After timeout:", tracker.exists(traffic))


if __name__ == "__main__":
    main()