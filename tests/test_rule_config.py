from core.rule_config import RuleConfigLoader


def main():
    loader = RuleConfigLoader()

    rules = loader.load("config/rules.json")

    print(f"Loaded rules: {len(rules)}")

    for rule in rules:
        print(rule)

    if len(rules) != 3:
        raise AssertionError(
            f"Expected 3 rules, got {len(rules)}"
        )

    print("Rule configuration test passed.")


if __name__ == "__main__":
    main()