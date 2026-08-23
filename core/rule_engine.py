import ipaddress

from core.rule import FirewallRule
from core.rule_validator import RuleValidator
from core.traffic import Traffic


class RuleEngine:
    def __init__(self):
        self.validator = RuleValidator()

    def ip_matches(self, rule_ip, traffic_ip):
        if rule_ip == "ANY":
            return True

        try:
            network = ipaddress.ip_network(rule_ip, strict=False)
            address = ipaddress.ip_address(traffic_ip)
            return address in network
        except ValueError:
            return rule_ip == traffic_ip

    def port_matches(self, rule_port, traffic_port):
        if rule_port is None:
            return True

        if traffic_port is None:
            return False

        if isinstance(rule_port, tuple):
            start, end = rule_port
            return start <= traffic_port <= end

        return rule_port == traffic_port

    def matches(self, rule: FirewallRule, traffic: Traffic):
        if not self.validator.validate(rule):
            return False

        if rule.direction != "ANY" and rule.direction != traffic.direction:
            return False

        if rule.protocol != "ANY" and rule.protocol != traffic.protocol:
            return False

        if not self.ip_matches(rule.source_ip, traffic.source_ip):
            return False

        if not self.ip_matches(rule.destination_ip, traffic.destination_ip):
            return False

        if not self.port_matches(rule.source_port, traffic.source_port):
            return False

        if not self.port_matches(
            rule.destination_port,
            traffic.destination_port
        ):
            return False

        return True

    def evaluate(self, rules, traffic):
        valid_rules = [
            rule for rule in rules
            if self.validator.validate(rule)
        ]

        ordered_rules = sorted(
            valid_rules,
            key=lambda rule: rule.priority
        )

        for rule in ordered_rules:
            if self.matches(rule, traffic):
                return rule.action

        return "BLOCK"