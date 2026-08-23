from dataclasses import dataclass
import time


@dataclass
class Connection:
    key: tuple
    state: str
    last_seen: float


class ConnectionTracker:
    def __init__(self, timeout=300):
        self.connections = {}
        self.timeout = timeout

    def _key(self, traffic):
        endpoint_a = (
            traffic.source_ip,
            traffic.source_port
        )

        endpoint_b = (
            traffic.destination_ip,
            traffic.destination_port
        )

        endpoints = tuple(sorted((endpoint_a, endpoint_b)))

        return (
            traffic.protocol,
            endpoints
        )

    def cleanup(self):
        now = time.time()

        expired = [
            key
            for key, connection in self.connections.items()
            if now - connection.last_seen > self.timeout
        ]

        for key in expired:
            del self.connections[key]

    def get_state(self, traffic):
        self.cleanup()

        connection = self.connections.get(self._key(traffic))

        if connection is None:
            return None

        return connection.state

    def update(self, traffic):
        self.cleanup()

        key = self._key(traffic)
        now = time.time()
        current = self.connections.get(key)

        if traffic.protocol == "UDP":
            state = "ACTIVE"

        elif traffic.protocol != "TCP":
            state = "ACTIVE"

        else:
            flags = traffic.tcp_flags or ""

            if "R" in flags:
                self.connections.pop(key, None)
                return "RESET"

            if "F" in flags:
                self.connections.pop(key, None)
                return "CLOSED"

            if "S" in flags and "A" not in flags:
                state = "SYN_SENT"
            elif "S" in flags and "A" in flags:
                state = "SYN_RECEIVED"
            elif "A" in flags:
                state = "ESTABLISHED"
            elif current:
                state = current.state
            else:
                state = "UNKNOWN"

        self.connections[key] = Connection(
            key=key,
            state=state,
            last_seen=now
        )

        return state

    def exists(self, traffic):
        return self.get_state(traffic) is not None

    def is_established(self, traffic):
        state = self.get_state(traffic)
        return state in ("ESTABLISHED", "ACTIVE")

    def remove(self, traffic):
        self.connections.pop(self._key(traffic), None)