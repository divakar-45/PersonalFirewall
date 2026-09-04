from config.monitoring import (
    LOG_FILE,
    ALERT_STATE_FILE,
    BLOCK_THRESHOLD,
    SOURCE_THRESHOLD,
    RECENT_EVENTS_COUNT
)

from core.alert_detector import AlertDetector
from core.alert_logger import AlertLogger
from core.alert_manager import AlertManager
from core.alert_reporter import AlertReporter
from core.log_analyzer import LogAnalyzer


class SecurityMonitor:
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

        self.alert_logger = AlertLogger()
        self.reporter = AlertReporter()

    def run(self):
        events = self.analyzer.load_events()

        recent_events = self.analyzer.recent_events(
            RECENT_EVENTS_COUNT
        )

        alerts = self.detector.detect(
            recent_events
        )

        new_alerts = self.manager.filter_new(
            alerts
        )

        print("EVENTS ANALYZED:", len(events))
        print(
            "RECENT EVENTS USED FOR DETECTION:",
            len(recent_events)
        )
        print("ALERTS DETECTED:", len(alerts))
        print("NEW ALERTS:", len(new_alerts))
        print()

        for alert in new_alerts:
            print(
                self.reporter.format_alert(alert)
            )
            print()

            self.alert_logger.log(alert)

        if not new_alerts:
            print("No new security alerts.")

        return new_alerts