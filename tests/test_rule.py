from core.rule import FirewallRule


def main():
    rule = FirewallRule(
        action="BLOCK",
        direction="INBOUND",
        protocol="TCP",
        destination_port=22
    )

    print(rule)


if __name__ == "__main__":
    main()