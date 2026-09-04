from collections import Counter, defaultdict


class AlertDetector:
    def __init__(
        self,
        block_threshold=5,
        source_threshold=5,
        port_scan_threshold=5
    ):
        self.block_threshold = block_threshold
        self.source_threshold = source_threshold
        self.port_scan_threshold = port_scan_threshold

    def excessive_blocks(self, events):
        blocked = [
            event
            for event in events
            if event.get("decision") == "BLOCK"
        ]

        if len(blocked) >= self.block_threshold:
            return {
                "type": "EXCESSIVE_BLOCKS",
                "severity": "MEDIUM",
                "message": (
                    f"{len(blocked)} blocked events detected"
                ),
                "count": len(blocked)
            }

        return None

    def repeated_blocked_sources(self, events):
        sources = Counter(
            event.get("source_ip", "UNKNOWN")
            for event in events
            if event.get("decision") == "BLOCK"
        )

        alerts = []

        for source_ip, count in sources.items():
            if count >= self.source_threshold:
                alerts.append({
                    "type": "REPEATED_BLOCKED_SOURCE",
                    "severity": "HIGH",
                    "source_ip": source_ip,
                    "count": count,
                    "message": (
                        f"Source {source_ip} generated "
                        f"{count} blocked events"
                    )
                })

        return alerts

    def repeated_blocked_destinations(self, events):
        destinations = Counter(
            event.get("destination_ip", "UNKNOWN")
            for event in events
            if event.get("decision") == "BLOCK"
        )

        alerts = []

        for destination_ip, count in destinations.items():
            if count >= self.block_threshold:
                alerts.append({
                    "type": "REPEATED_BLOCKED_DESTINATION",
                    "severity": "MEDIUM",
                    "destination_ip": destination_ip,
                    "count": count,
                    "message": (
                        f"Destination {destination_ip} "
                        f"appeared in {count} blocked events"
                    )
                })

        return alerts

    def port_scan_detection(self, events):
        blocked_ports = defaultdict(set)

        for event in events:
            if event.get("decision") != "BLOCK":
                continue

            if event.get("protocol") != "TCP":
                continue

            source_ip = event.get(
                "source_ip",
                "UNKNOWN"
            )

            destination_port = event.get(
                "destination_port"
            )

            if destination_port is None:
                continue

            blocked_ports[source_ip].add(
                destination_port
            )

        alerts = []

        for source_ip, ports in blocked_ports.items():
            if len(ports) >= self.port_scan_threshold:
                alerts.append({
                    "type": "PORT_SCAN",
                    "severity": "HIGH",
                    "source_ip": source_ip,
                    "ports": sorted(ports),
                    "port_count": len(ports),
                    "message": (
                        f"Source {source_ip} attempted "
                        f"connections to {len(ports)} "
                        f"different blocked TCP ports"
                    )
                })

        return alerts

    def detect(self, events):
        alerts = []

        excessive_blocks = self.excessive_blocks(
            events
        )

        if excessive_blocks:
            alerts.append(excessive_blocks)

        alerts.extend(
            self.repeated_blocked_sources(events)
        )

        alerts.extend(
            self.repeated_blocked_destinations(events)
        )

        alerts.extend(
            self.port_scan_detection(events)
        )

        return alerts