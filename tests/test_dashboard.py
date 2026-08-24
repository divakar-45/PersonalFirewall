from core.dashboard import SecurityDashboard


def main():
    dashboard = SecurityDashboard()

    data = dashboard.display()

    print()
    print("Dashboard generated successfully.")
    print("Events:", len(data["events"]))
    print("Alerts:", len(data["alerts"]))


if __name__ == "__main__":
    main()