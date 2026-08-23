from core.rule import FirewallRule
from core.rule_validator import RuleValidator


def main():
    validator = RuleValidator()

    valid_rule = FirewallRule(
        action="BLOCK",
        direction="INBOUND",
        protocol="TCP",
        source_ip="192.168.1.0/24",
        destination_port=(8000, 8080)
    )

    invalid_action = FirewallRule(
        action="DENY"
    )

    invalid_port = FirewallRule(
        action="BLOCK",
        destination_port=70000
    )

    invalid_range = FirewallRule(
        action="BLOCK",
        destination_port=(9000, 8000)
    )

    invalid_protocol = FirewallRule(
        action="BLOCK",
        protocol="XYZ"
    )

    print("Valid rule:", validator.validate(valid_rule))
    print("Invalid action:", validator.validate(invalid_action))
    print("Invalid port:", validator.validate(invalid_port))
    print("Invalid range:", validator.validate(invalid_range))
    print("Invalid protocol:", validator.validate(invalid_protocol))


if __name__ == "__main__":
    main()