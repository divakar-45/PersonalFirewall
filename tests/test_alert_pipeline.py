from core.alert_detector import AlertDetector
from core.alert_logger import AlertLogger
from core.alert_manager import AlertManager
from core.log_analyzer import LogAnalyzer


def main():
    analyzer = LogAnalyzer()

    detector = AlertDetector(
        block_threshold=5,
        source_threshold=5
    )

    manager = AlertManager(
        state_file="logs/alert_state.json"
    )

    alert_logger = AlertLogger()

    events = analyzer.load_events()

    alerts = detector.detect(events)

    new_alerts = manager.filter_new(alerts)

    print("EVENTS ANALYZED:", len(events))
    print("ALERTS DETECTED:", len(alerts))
    print("NEW ALERTS:", len(new_alerts))
    print()

    for alert in new_alerts:
        print("NEW ALERT:", alert)
        alert_logger.log(alert)

    print()
    print("Alert pipeline completed successfully.")


if __name__ == "__main__":
    main()