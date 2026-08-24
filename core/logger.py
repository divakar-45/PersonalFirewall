import json
import logging
from datetime import datetime, timezone
from pathlib import Path


class FirewallLogger:
    def __init__(self, log_file="logs/firewall.log"):
        self.log_file = Path(log_file)

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.logger = logging.getLogger("personal_firewall")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8"
            )

            handler.setFormatter(
                logging.Formatter("%(message)s")
            )

            self.logger.addHandler(handler)

    def log(self, traffic, state, decision):
        event = {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "direction": traffic.direction,
            "protocol": traffic.protocol,
            "source_ip": traffic.source_ip,
            "source_port": traffic.source_port,
            "destination_ip": traffic.destination_ip,
            "destination_port": traffic.destination_port,
            "state": state or "NEW",
            "decision": decision,
            "tcp_flags": traffic.tcp_flags
        }

        self.logger.info(
            json.dumps(event)
        )