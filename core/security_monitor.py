from core.alert_detector import AlertDetector
from core.alert_logger import AlertLogger
from core.alert_manager import AlertManager
from core.alert_reporter import AlertReporter
from core.log_analyzer import LogAnalyzer


class SecurityMonitor:
    def __init__(
        self,
        log_file="logs/firewall.log",
        state_file="logs/alert_state.json"
    ):
        self.analyzer = LogAnalyzer(log_file)

        self.detector = AlertDetector(
            block_threshold=5,
            source_threshold=5
        )

        self.manager = AlertManager(
            state_file=state_file
        )

        self.alert_logger = AlertLogger()
        self.reporter = AlertReporter()

    def run(self):
        events = self.analyzer.load_events()

        alerts = self.detector.detect(events)

        new_alerts = self.manager.filter_new(alerts)

        print("EVENTS ANALYZED:", len(events))
        print("ALERTS DETECTED:", len(alerts))
        print("NEW ALERTS:", len(new_alerts))
        print()

        for alert in new_alerts:
            print(self.reporter.format_alert(alert))
            print()

            self.alert_logger.log(alert)

        if not new_alerts:
            print("No new security alerts.")

        return new_alerts