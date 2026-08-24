from core.alert_reporter import AlertReporter


def main():
    reporter = AlertReporter()

    alerts = [
        {
            "type": "EXCESSIVE_BLOCKS",
            "severity": "MEDIUM",
            "message": "10 blocked events detected",
            "count": 10
        },
        {
            "type": "REPEATED_BLOCKED_SOURCE",
            "severity": "HIGH",
            "source_ip": "192.168.1.50",
            "count": 6,
            "message": "Repeated blocked source detected"
        }
    ]

    print(reporter.format_alerts(alerts))


if __name__ == "__main__":
    main()