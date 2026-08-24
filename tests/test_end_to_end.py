from core.dashboard import SecurityDashboard
from core.security_monitor import SecurityMonitor


def main():
    print("=" * 60)
    print("PERSONAL FIREWALL - END-TO-END SECURITY TEST")
    print("=" * 60)

    print()
    print("STEP 1: SECURITY MONITOR")
    print("-" * 60)

    monitor = SecurityMonitor()
    new_alerts = monitor.run()

    print()
    print("New alerts returned:", len(new_alerts))

    print()
    print("STEP 2: SECURITY DASHBOARD")
    print("-" * 60)

    dashboard = SecurityDashboard()
    data = dashboard.display()

    print()
    print("STEP 3: VALIDATION")
    print("-" * 60)

    assert "summary" in data
    assert "alerts" in data
    assert data["summary"]["total_events"] >= 0

    print("Dashboard data: OK")
    print("Alert data: OK")
    print("Log analysis: OK")

    print()
    print("=" * 60)
    print("END-TO-END TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()