from core.log_analyzer import LogAnalyzer


def main():
    analyzer = LogAnalyzer()

    print("TOTAL EVENTS:")
    print(analyzer.total_events())

    print()
    print("DECISIONS:")
    print(analyzer.decision_counts())

    print()
    print("DIRECTIONS:")
    print(analyzer.direction_counts())

    print()
    print("PROTOCOLS:")
    print(analyzer.protocol_counts())

    print()
    print("BLOCKED DESTINATIONS:")
    print(analyzer.blocked_destinations())

    print()
    print("RECENT EVENTS:")
    for event in analyzer.recent_events(5):
        print(event)

    print()
    print("SUMMARY:")
    print(analyzer.summary())


if __name__ == "__main__":
    main()
    