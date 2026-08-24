from core.alert_detector import AlertDetector
from core.alert_logger import AlertLogger
from core.log_analyzer import LogAnalyzer


def main():
    analyzer = LogAnalyzer()
    detector = AlertDetector(
        block_threshold=5,
        source_threshold=5
    )
    alert_logger = AlertLogger()

    events = analyzer.load_events()

    alerts = detector.detect(events)

    print("EVENTS ANALYZED:", len(events))
    print("ALERTS DETECTED:", len(alerts))
    print()

    for alert in alerts:
        print("ALERT:", alert)
        alert_logger.log(alert)

    print()
    print("Alert pipeline completed successfully.")


if __name__ == "__main__":
    main()