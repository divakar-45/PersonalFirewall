from core.rule import FirewallRule
from core.rule_config import RuleConfigLoader


def main():
    loader = RuleConfigLoader()

    config_file = "logs/test_rules.json"

    rules = [
        FirewallRule(
            action="ALLOW",
            priority=10,
            direction="OUTBOUND",
            protocol="TCP",
            destination_port=443
        ),
        FirewallRule(
            action="BLOCK",
            priority=100,
            direction="ANY",
            protocol="TCP",
            destination_port=(8000, 9000)
        )
    ]

    loader.save(config_file, rules)

    loaded_rules = loader.load(config_file)

    if len(loaded_rules) != 2:
        raise AssertionError(
            f"Expected 2 rules, got {len(loaded_rules)}"
        )

    new_rule = FirewallRule(
        action="ALLOW",
        priority=5,
        direction="OUTBOUND",
        protocol="UDP",
        destination_port=53
    )

    loader.add_rule(
        loaded_rules,
        new_rule
    )

    if loaded_rules[0] != new_rule:
        raise AssertionError(
            "Rules were not sorted by priority."
        )

    loader.remove_rule(
        loaded_rules,
        0
    )

    if len(loaded_rules) != 2:
        raise AssertionError(
            "Rule removal failed."
        )

    listed_rules = loader.list_rules(
        loaded_rules
    )

    if len(listed_rules) != 2:
        raise AssertionError(
            "Rule listing failed."
        )

    print("Rule management test passed.")
    print(f"Rules remaining: {len(listed_rules)}")


if __name__ == "__main__":
    main()