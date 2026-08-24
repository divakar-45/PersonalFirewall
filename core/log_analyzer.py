import json
from collections import Counter
from pathlib import Path


class LogAnalyzer:
    def __init__(self, log_file="logs/firewall.log"):
        self.log_file = Path(log_file)

    def load_events(self):
        if not self.log_file.exists():
            return []

        events = []

        with self.log_file.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

        return events

    def total_events(self):
        return len(self.load_events())

    def decision_counts(self):
        events = self.load_events()

        return dict(
            Counter(
                event.get("decision", "UNKNOWN")
                for event in events
            )
        )

    def direction_counts(self):
        events = self.load_events()

        return dict(
            Counter(
                event.get("direction", "UNKNOWN")
                for event in events
            )
        )

    def protocol_counts(self):
        events = self.load_events()

        return dict(
            Counter(
                event.get("protocol", "UNKNOWN")
                for event in events
            )
        )

    def blocked_destinations(self):
        events = self.load_events()

        return dict(
            Counter(
                event.get("destination_ip", "UNKNOWN")
                for event in events
                if event.get("decision") == "BLOCK"
            )
        )

    def recent_events(self, count=10):
        events = self.load_events()

        return events[-count:]

    def summary(self):
        return {
            "total_events": self.total_events(),
            "decisions": self.decision_counts(),
            "directions": self.direction_counts(),
            "protocols": self.protocol_counts(),
            "blocked_destinations": self.blocked_destinations()
        }