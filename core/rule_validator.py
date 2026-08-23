import ipaddress

from core.rule import FirewallRule


class RuleValidator:
    VALID_ACTIONS = {"ALLOW", "BLOCK"}
    VALID_DIRECTIONS = {"ANY", "INBOUND", "OUTBOUND"}
    VALID_PROTOCOLS = {"ANY", "TCP", "UDP", "ICMP"}

    def validate(self, rule: FirewallRule):
        if not isinstance(rule.priority, int) or rule.priority < 0:
            return False

        if rule.action not in self.VALID_ACTIONS:
            return False

        if rule.direction not in self.VALID_DIRECTIONS:
            return False

        if rule.protocol not in self.VALID_PROTOCOLS:
            return False

        if not self.valid_ip(rule.source_ip):
            return False

        if not self.valid_ip(rule.destination_ip):
            return False

        if not self.valid_port(rule.source_port):
            return False

        if not self.valid_port(rule.destination_port):
            return False

        return True

    def valid_ip(self, value):
        if value == "ANY":
            return True

        try:
            ipaddress.ip_network(value, strict=False)
            return True
        except ValueError:
            return False

    def valid_port(self, value):
        if value is None:
            return True

        if isinstance(value, tuple):
            if len(value) != 2:
                return False

            start, end = value

            if not isinstance(start, int) or not isinstance(end, int):
                return False

            return 1 <= start <= end <= 65535

        return isinstance(value, int) and 1 <= value <= 65535