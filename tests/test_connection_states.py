from core.connection_tracker import ConnectionTracker
from core.traffic import Traffic


def create_traffic(flags, direction, source_port=50000, destination_port=443):
    if direction == "OUTBOUND":
        source_ip = "10.77.190.132"
        destination_ip = "142.250.1.1"
    else:
        source_ip = "142.250.1.1"
        destination_ip = "10.77.190.132"

    return Traffic(
        source_ip=source_ip,
        destination_ip=destination_ip,
        protocol="TCP",
        source_port=source_port if direction == "OUTBOUND" else destination_port,
        destination_port=destination_port if direction == "OUTBOUND" else source_port,
        direction=direction,
        tcp_flags=flags
    )


def main():
    tracker = ConnectionTracker()

    syn = create_traffic("S", "OUTBOUND")
    syn_ack = create_traffic("SA", "INBOUND")
    ack = create_traffic("A", "OUTBOUND")
    data = create_traffic("PA", "INBOUND")
    fin = create_traffic("FA", "OUTBOUND")

    print("SYN:", tracker.update(syn))
    print("SYN-ACK:", tracker.update(syn_ack))
    print("ACK:", tracker.update(ack))
    print("DATA:", tracker.update(data))
    print("FIN:", tracker.update(fin))


if __name__ == "__main__":
    main()