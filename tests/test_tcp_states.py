from core.traffic import Traffic


def main():
    syn = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="S"
    )

    syn_ack = Traffic(
        source_ip="142.250.1.1",
        destination_ip="10.77.190.132",
        protocol="TCP",
        source_port=443,
        destination_port=50000,
        direction="INBOUND",
        tcp_flags="SA"
    )

    ack = Traffic(
        source_ip="10.77.190.132",
        destination_ip="142.250.1.1",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="OUTBOUND",
        tcp_flags="A"
    )

    established = Traffic(
        source_ip="142.250.1.1",
        destination_ip="10.77.190.132",
        protocol="TCP",
        source_port=443,
        destination_port=50000,
        direction="INBOUND",
        tcp_flags="PA"
    )

    print("SYN:", syn.tcp_flags)
    print("SYN-ACK:", syn_ack.tcp_flags)
    print("ACK:", ack.tcp_flags)
    print("ESTABLISHED DATA:", established.tcp_flags)


if __name__ == "__main__":
    main()
    