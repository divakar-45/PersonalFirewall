from core.alert_detector import AlertDetector


def main():
    detector = AlertDetector(
        block_threshold=5,
        source_threshold=5,
        port_scan_threshold=5
    )

    events = [
        {
            "source_ip": "192.168.1.50",
            "destination_ip": "192.168.1.10",
            "destination_port": 21,
            "protocol": "TCP",
            "decision": "BLOCK"
        },
        {
            "source_ip": "192.168.1.50",
            "destination_ip": "192.168.1.10",
            "destination_port": 22,
            "protocol": "TCP",
            "decision": "BLOCK"
        },
        {
            "source_ip": "192.168.1.50",
            "destination_ip": "192.168.1.10",
            "destination_port": 23,
            "protocol": "TCP",
            "decision": "BLOCK"
        },
        {
            "source_ip": "192.168.1.50",
            "destination_ip": "192.168.1.10",
            "destination_port": 80,
            "protocol": "TCP",
            "decision": "BLOCK"
        },
        {
            "source_ip": "192.168.1.50",
            "destination_ip": "192.168.1.10",
            "destination_port": 443,
            "protocol": "TCP",
            "decision": "BLOCK"
        }
    ]

    alerts = detector.port_scan_detection(events)

    if len(alerts) != 1:
        raise AssertionError(
            f"Expected 1 port scan alert, got {len(alerts)}"
        )

    alert = alerts[0]

    if alert["type"] != "PORT_SCAN":
        raise AssertionError(
            "Incorrect alert type."
        )

    if alert["severity"] != "HIGH":
        raise AssertionError(
            "Incorrect alert severity."
        )

    if alert["source_ip"] != "192.168.1.50":
        raise AssertionError(
            "Incorrect source IP."
        )

    if alert["port_count"] != 5:
        raise AssertionError(
            "Incorrect port count."
        )

    expected_ports = [21, 22, 23, 80, 443]

    if alert["ports"] != expected_ports:
        raise AssertionError(
            "Incorrect detected ports."
        )

    print("Port scan detection test passed.")
    print("Source:", alert["source_ip"])
    print("Ports:", alert["ports"])
    print("Severity:", alert["severity"])


if __name__ == "__main__":
    main()