from config.monitoring import (
    LOG_FILE,
    ALERT_STATE_FILE,
    BLOCK_THRESHOLD,
    SOURCE_THRESHOLD,
)

from core.alert_detector import AlertDetector
from core.alert_manager import AlertManager
from core.log_analyzer import LogAnalyzer


class SecurityDashboard:
    def __init__(
        self,
        log_file=LOG_FILE,
        state_file=ALERT_STATE_FILE
    ):
        self.analyzer = LogAnalyzer(log_file)

        self.detector = AlertDetector(
            block_threshold=BLOCK_THRESHOLD,
            source_threshold=SOURCE_THRESHOLD
        )

        self.manager = AlertManager(
            state_file=state_file
        )

    def generate(self):
        events = self.analyzer.load_events()
        summary = self.analyzer.summary()
        alerts = self.detector.detect(events)

        return {
        "events": events,
        "summary": summary,
        "alerts": alerts
    }

    def display(self):
        data = self.generate()

        summary = data["summary"]
        alerts = data["alerts"]

        print()
        print("=" * 50)
        print("             FIREWALL SECURITY DASHBOARD")
        print("=" * 50)

        print()
        print("TRAFFIC OVERVIEW")
        print("-" * 50)
        print("Total Events:", summary["total_events"])
        print("Allowed:", summary["decisions"].get("ALLOW", 0))
        print("Blocked:", summary["decisions"].get("BLOCK", 0))

        print()
        print("DIRECTION")
        print("-" * 50)

        for direction, count in summary["directions"].items():
            print(f"{direction}: {count}")

        print()
        print("PROTOCOLS")
        print("-" * 50)

        for protocol, count in summary["protocols"].items():
            print(f"{protocol}: {count}")

        print()
        print("SECURITY ALERTS")
        print("-" * 50)
        print("Alerts Detected:", len(alerts))

        severity_counts = {}

        for alert in alerts:
            severity = alert.get("severity", "UNKNOWN")

            severity_counts[severity] = (
                severity_counts.get(severity, 0) + 1
            )

        for severity, count in severity_counts.items():
            print(f"{severity}: {count}")

        print()
        print("RECENT ALERTS")
        print("-" * 50)

        if not alerts:
            print("No alerts detected.")
        else:
            for alert in alerts:
                print(
                    f"[{alert.get('severity', 'UNKNOWN')}] "
                    f"{alert.get('type', 'UNKNOWN')} - "
                    f"{alert.get('message', '')}"
                )

        print()
        print("=" * 50)

        return data