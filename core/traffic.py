from dataclasses import dataclass


@dataclass
class Traffic:
    source_ip: str
    destination_ip: str
    protocol: str
    source_port: int | None
    destination_port: int | None
    direction: str
    tcp_flags: str | None = None