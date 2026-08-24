from core.alert_detector import AlertDetector
from core.log_analyzer import LogAnalyzer


def main():
    analyzer = LogAnalyzer()
    detector = AlertDetector(
        block_threshold=5,
        source_threshold=5
    )

    events = analyzer.load_events()

    print("EVENTS:", len(events))
    print()

    print("EXCESSIVE BLOCKS:")
    print(detector.excessive_blocks(events))

    print()
    print("REPEATED BLOCKED SOURCES:")
    for alert in detector.repeated_blocked_sources(events):
        print(alert)

    print()
    print("REPEATED BLOCKED DESTINATIONS:")
    for alert in detector.repeated_blocked_destinations(events):
        print(alert)

    print()
    print("ALL ALERTS:")
    for alert in detector.detect(events):
        print(alert)


if __name__ == "__main__":
    main()