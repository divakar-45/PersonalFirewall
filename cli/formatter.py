def format_traffic(traffic):
    if traffic is None:
        return "Unsupported packet"

    source = traffic.source_ip

    if traffic.source_port is not None:
        source = f"{source}:{traffic.source_port}"

    destination = traffic.destination_ip

    if traffic.destination_port is not None:
        destination = f"{destination}:{traffic.destination_port}"

    return f"[{traffic.direction}] {traffic.protocol} {source} -> {destination}"