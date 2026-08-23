from dataclasses import dataclass


@dataclass
class FirewallRule:
    action: str
    priority: int = 100
    direction: str = "ANY"
    protocol: str = "ANY"
    source_ip: str = "ANY"
    destination_ip: str = "ANY"
    source_port: int | tuple[int, int] | None = None
    destination_port: int | tuple[int, int] | None = None