from core.security_monitor import SecurityMonitor


def main():
    monitor = SecurityMonitor()

    alerts = monitor.run()

    print()
    print("NEW ALERTS:", len(alerts))


if __name__ == "__main__":
    main()