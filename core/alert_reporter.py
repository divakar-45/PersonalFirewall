from datetime import datetime


class AlertReporter:
    def format_alert(self, alert):
        severity = alert.get("severity", "UNKNOWN")
        alert_type = alert.get("type", "UNKNOWN")
        message = alert.get("message", "No message")

        lines = [
            "========================================",
            "           FIREWALL SECURITY ALERT",
            "========================================",
            f"Time:     {datetime.now().isoformat()}",
            f"Type:     {alert_type}",
            f"Severity: {severity}",
            f"Message:  {message}",
        ]

        if "source_ip" in alert:
            lines.append(
                f"Source:   {alert['source_ip']}"
            )

        if "destination_ip" in alert:
            lines.append(
                f"Target:   {alert['destination_ip']}"
            )

        if "count" in alert:
            lines.append(
                f"Count:    {alert['count']}"
            )

        lines.append(
            "========================================"
        )

        return "\n".join(lines)

    def format_alerts(self, alerts):
        if not alerts:
            return "No security alerts detected."

        return "\n\n".join(
            self.format_alert(alert)
            for alert in alerts
        )