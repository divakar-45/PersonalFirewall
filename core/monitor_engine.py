import json
import time
from pathlib import Path

from core.alert_detector import AlertDetector
from core.alert_logger import AlertLogger
from core.alert_manager import AlertManager
from core.alert_reporter import AlertReporter


class MonitorEngine:
    def __init__(
        self,
        log_file="logs/firewall.log",
        poll_interval=2
    ):
        self.log_file = Path(log_file)
        self.poll_interval = poll_interval

        self.detector = AlertDetector(
            block_threshold=5,
            source_threshold=5
        )

        self.manager = AlertManager(
            state_file="logs/alert_state.json"
        )

        self.alert_logger = AlertLogger()
        self.reporter = AlertReporter()

        self.position = self._get_current_position()
        self.events = []

    def _get_current_position(self):
        if not self.log_file.exists():
            return 0

        return self.log_file.stat().st_size

    def _read_new_events(self):
        if not self.log_file.exists():
            return []

        new_events = []

        with self.log_file.open(
            "r",
            encoding="utf-8"
        ) as file:

            file.seek(self.position)

            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    event = json.loads(line)
                    new_events.append(event)
                except json.JSONDecodeError:
                    continue

            self.position = file.tell()

        return new_events

    def process_events(self, events):
        if not events:
            return []

        self.events.extend(events)

        alerts = self.detector.detect(
            self.events
        )

        new_alerts = self.manager.filter_new(
            alerts
        )

        for alert in new_alerts:
            self.alert_logger.log(alert)

            print()
            print(
                self.reporter.format_alert(alert)
            )
            print()

        return new_alerts

    def run_once(self):
        events = self._read_new_events()

        return self.process_events(events)

    def run(self):
        print("=" * 50)
        print("        FIREWALL SECURITY MONITOR")
        print("=" * 50)
        print()
        print("Monitoring:", self.log_file)
        print("Poll interval:", self.poll_interval, "seconds")
        print()
        print("Monitor started.")
        print("Press Ctrl+C to stop.")
        print()

        try:
            while True:
                new_alerts = self.run_once()

                if new_alerts:
                    print(
                        f"New alerts detected: "
                        f"{len(new_alerts)}"
                    )

                time.sleep(
                    self.poll_interval
                )

        except KeyboardInterrupt:
            print()
            print("Monitor stopped.")