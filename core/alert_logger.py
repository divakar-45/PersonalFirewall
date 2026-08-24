import json
import logging
from datetime import datetime, timezone
from pathlib import Path


class AlertLogger:
    def __init__(self, log_file="logs/alerts.log"):
        self.log_file = Path(log_file)

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.logger = logging.getLogger("personal_firewall_alerts")
        self.logger.setLevel(logging.WARNING)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8"
            )

            handler.setFormatter(
                logging.Formatter("%(message)s")
            )

            self.logger.addHandler(handler)

    def log(self, alert):
        event = {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            **alert
        }

        self.logger.warning(
            json.dumps(event)
        )