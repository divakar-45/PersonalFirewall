from core.alert_manager import AlertManager


def main():
    manager = AlertManager(
        state_file="logs/test_alert_state.json"
    )

    alert = {
        "type": "TEST_ALERT",
        "severity": "HIGH",
        "message": "Repeated alert test",
        "count": 5
    }

    print("FIRST CHECK:")
    print(manager.is_new(alert))

    print()
    print("SECOND CHECK:")
    print(manager.is_new(alert))

    print()
    print("FILTER TEST:")

    alerts = [
        alert,
        alert,
        {
            "type": "SECOND_ALERT",
            "severity": "MEDIUM",
            "message": "Another alert",
            "count": 1
        }
    ]

    new_alerts = manager.filter_new(alerts)

    print("NEW ALERTS:", len(new_alerts))

    for item in new_alerts:
        print(item)


if __name__ == "__main__":
    main()