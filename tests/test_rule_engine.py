from core.rule import FirewallRule
from core.rule_engine import RuleEngine
from core.traffic import Traffic


def main():
    engine = RuleEngine()

    rules = [
        FirewallRule(
            action="ALLOW",
            priority=200,
            direction="INBOUND",
            protocol="TCP",
            destination_port=443
        ),
        FirewallRule(
            action="BLOCK",
            priority=10,
            direction="INBOUND",
            protocol="TCP",
            destination_port=443
        )
    ]

    traffic = Traffic(
        source_ip="10.0.0.5",
        destination_ip="192.168.1.10",
        protocol="TCP",
        source_port=50000,
        destination_port=443,
        direction="INBOUND"
    )

    print("Decision:", engine.evaluate(rules, traffic))


if __name__ == "__main__":
    main()