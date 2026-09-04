import json
from pathlib import Path

from core.monitor_engine import MonitorEngine


TEST_LOG = Path("logs/test_monitor_engine.log")
TEST_STATE = Path("logs/test_monitor_engine_alert_state.json")


def write_event(source_ip, destination_port):
    event = {
        "timestamp": "2026-09-02T00:00:00+00:00",
        "direction": "OUTBOUND",
        "protocol": "TCP",
        "source_ip": source_ip,
        "source_port": 50000,
        "destination_ip": "192.168.1.10",
        "destination_port": destination_port,
        "state": "NEW",
        "decision": "BLOCK",
        "tcp_flags": "S"
    }

    with TEST_LOG.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")


def main():
    TEST_LOG.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Start every test with a clean log and clean alert state.
    TEST_LOG.write_text(
        "",
        encoding="utf-8"
    )

    TEST_STATE.unlink(
        missing_ok=True
    )

    monitor = MonitorEngine(
        log_file=TEST_LOG,
        poll_interval=1,
        state_file=TEST_STATE
    )

    # Monitor starts at the current end of the file.
    assert monitor.run_once() == []

    # Add five different blocked TCP ports.
    for port in [21, 22, 23, 80, 443]:
        write_event(
            "192.168.1.50",
            port
        )

    alerts = monitor.run_once()

    assert len(alerts) >= 1

    port_scan_alerts = [
        alert
        for alert in alerts
        if alert["type"] == "PORT_SCAN"
    ]

    assert len(port_scan_alerts) == 1

    alert = port_scan_alerts[0]

    assert alert["source_ip"] == "192.168.1.50"
    assert alert["port_count"] == 5
    assert alert["ports"] == [21, 22, 23, 80, 443]
    assert alert["severity"] == "HIGH"

    # Reading again without adding events should produce nothing.
    assert monitor.run_once() == []

    print("MonitorEngine test passed.")
    print("New events processed: 5")
    print("Port scan detected:", alert["source_ip"])
    print("Ports:", alert["ports"])
    print("Duplicate processing prevented.")


if __name__ == "__main__":
    main()