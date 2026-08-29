import json
from pathlib import Path

from core.firewall import Firewall
from core.rule import FirewallRule


def main():
    test_config = "logs/test_firewall_rules.json"

    Path(test_config).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    initial_rules = [
        FirewallRule(
            action="ALLOW",
            priority=10,
            direction="OUTBOUND",
            protocol="TCP",
            destination_port=443
        ),
        FirewallRule(
            action="BLOCK",
            priority=1000,
            direction="ANY",
            protocol="ANY"
        )
    ]

    with open(
        test_config,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            [
                {
                    "action": rule.action,
                    "priority": rule.priority,
                    "direction": rule.direction,
                    "protocol": rule.protocol,
                    "source_ip": rule.source_ip,
                    "destination_ip": rule.destination_ip,
                    "source_port": rule.source_port,
                    "destination_port": rule.destination_port
                }
                for rule in initial_rules
            ],
            file,
            indent=4
        )

    firewall = Firewall(
        rule_file=test_config
    )

    initial_count = len(
        firewall.list_rules()
    )

    test_rule = FirewallRule(
        action="ALLOW",
        priority=5,
        direction="OUTBOUND",
        protocol="TCP",
        destination_port=8443
    )

    firewall.add_rule(test_rule)

    rules_after_add = firewall.list_rules()

    if len(rules_after_add) != initial_count + 1:
        raise AssertionError(
            "Firewall.add_rule() failed."
        )

    if rules_after_add[0] != test_rule:
        raise AssertionError(
            "Firewall rules are not sorted by priority."
        )

    with open(
        test_config,
        "r",
        encoding="utf-8"
    ) as file:
        saved_rules = json.load(file)

    if len(saved_rules) != initial_count + 1:
        raise AssertionError(
            "Added rule was not persisted."
        )

    firewall.remove_rule(0)

    rules_after_remove = firewall.list_rules()

    if len(rules_after_remove) != initial_count:
        raise AssertionError(
            "Firewall.remove_rule() failed."
        )

    with open(
        test_config,
        "r",
        encoding="utf-8"
    ) as file:
        saved_rules = json.load(file)

    if len(saved_rules) != initial_count:
        raise AssertionError(
            "Removed rule was not persisted."
        )

    print("Firewall rule management test passed.")
    print("Add, list, remove, and persistence verified.")


if __name__ == "__main__":
    main()