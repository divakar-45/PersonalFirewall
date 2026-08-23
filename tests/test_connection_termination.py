from core.connection_tracker import ConnectionTracker
from core.traffic import Traffic


def main():
    tracker = ConnectionTracker()

    traffic = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="A"
    )

    fin = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="FA"
    )

    rst = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="R"
    )

    tracker.update(traffic)

    print("Before FIN:", tracker.exists(traffic))

    print("FIN state:", tracker.update(fin))

    print("After FIN:", tracker.exists(traffic))

    tracker.update(traffic)

    print("Before RST:", tracker.exists(traffic))

    print("RST state:", tracker.update(rst))

    print("After RST:", tracker.exists(traffic))


if __name__ == "__main__":
    main()