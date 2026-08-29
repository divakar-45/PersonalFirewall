import json
from dataclasses import asdict
from pathlib import Path

from core.rule import FirewallRule
from core.rule_validator import RuleValidator


class RuleConfigLoader:
    def __init__(self):
        self.validator = RuleValidator()

    def load(self, config_file):
        path = Path(config_file)

        if not path.exists():
            raise FileNotFoundError(
                f"Rule configuration not found: {path}"
            )

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError(
                "Rule configuration must contain a JSON list."
            )

        rules = []

        for index, item in enumerate(data):
            if not isinstance(item, dict):
                raise ValueError(
                    f"Rule at index {index} must be an object."
                )

            rule = FirewallRule(
                action=item.get("action"),
                priority=item.get("priority", 100),
                direction=item.get("direction", "ANY"),
                protocol=item.get("protocol", "ANY"),
                source_ip=item.get("source_ip", "ANY"),
                destination_ip=item.get("destination_ip", "ANY"),
                source_port=self._parse_port(
                    item.get("source_port")
                ),
                destination_port=self._parse_port(
                    item.get("destination_port")
                )
            )

            if not self.validator.validate(rule):
                raise ValueError(
                    f"Invalid firewall rule at index {index}: {rule}"
                )

            rules.append(rule)

        return rules

    def save(self, config_file, rules):
        path = Path(config_file)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        for index, rule in enumerate(rules):
            if not self.validator.validate(rule):
                raise ValueError(
                    f"Invalid firewall rule at index {index}: {rule}"
                )

        data = [
            self._rule_to_dict(rule)
            for rule in rules
        ]

        with path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4
            )

    def add_rule(self, rules, rule):
        if not self.validator.validate(rule):
            raise ValueError(
                f"Invalid firewall rule: {rule}"
            )

        rules.append(rule)

        rules.sort(
            key=lambda item: item.priority
        )

        return rules

    def remove_rule(self, rules, index):
        if not isinstance(index, int):
            raise TypeError(
                "Rule index must be an integer."
            )

        if index < 0 or index >= len(rules):
            raise IndexError(
                f"Rule index out of range: {index}"
            )

        rules.pop(index)

        return rules

    def list_rules(self, rules):
        return list(rules)

    def _rule_to_dict(self, rule):
        data = asdict(rule)

        if isinstance(data["source_port"], tuple):
            data["source_port"] = list(
                data["source_port"]
            )

        if isinstance(data["destination_port"], tuple):
            data["destination_port"] = list(
                data["destination_port"]
            )

        return data

    def _parse_port(self, value):
        if value is None:
            return None

        if isinstance(value, int):
            return value

        if isinstance(value, list):
            if len(value) != 2:
                raise ValueError(
                    "Port range must contain exactly two values."
                )

            return tuple(value)

        raise ValueError(
            f"Invalid port value: {value}"
        )