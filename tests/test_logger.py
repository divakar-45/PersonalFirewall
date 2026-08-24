from core.logger import FirewallLogger
from core.traffic import Traffic


def main():
    logger = FirewallLogger()

    traffic = Traffic(
        source_ip="10.77.190.132",
        destination_ip="8.8.8.8",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="S"
    )

    logger.log(
        traffic,
        "SYN_SENT",
        "ALLOW"
    )

    print("Log event written successfully.")


if __name__ == "__main__":
    main()