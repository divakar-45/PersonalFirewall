from core.firewall import Firewall
from core.rule import FirewallRule


def main():
    firewall = Firewall()

    firewall.add_rule(
        FirewallRule(
            action="ALLOW",
            priority=10,
            direction="OUTBOUND",
            protocol="TCP",
            destination_port=443
        )
    )

    firewall.process(count=10)


if __name__ == "__main__":
    main()