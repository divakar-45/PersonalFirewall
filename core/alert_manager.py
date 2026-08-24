import hashlib
import json
from pathlib import Path


class AlertManager:
    def __init__(self, state_file="logs/alert_state.json"):
        self.state_file = Path(state_file)

        self.state_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.seen_alerts = self._load_state()

    def _load_state(self):
        if not self.state_file.exists():
            return set()

        try:
            with self.state_file.open(
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            return set(data)

        except (json.JSONDecodeError, OSError):
            return set()

    def _save_state(self):
        with self.state_file.open(
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                sorted(self.seen_alerts),
                file,
                indent=2
            )

    def _fingerprint(self, alert):
        normalized = json.dumps(
            alert,
            sort_keys=True
        )

        return hashlib.sha256(
            normalized.encode("utf-8")
        ).hexdigest()

    def is_new(self, alert):
        fingerprint = self._fingerprint(alert)

        if fingerprint in self.seen_alerts:
            return False

        self.seen_alerts.add(fingerprint)
        self._save_state()

        return True

    def filter_new(self, alerts):
        new_alerts = []

        for alert in alerts:
            if self.is_new(alert):
                new_alerts.append(alert)

        return new_alerts