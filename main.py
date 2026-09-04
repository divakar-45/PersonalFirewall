from core.firewall import Firewall


def main():
    print("=" * 50)
    print("             PERSONAL FIREWALL")
    print("=" * 50)
    print()

    firewall = Firewall()

    print("Firewall initialized.")
    print(f"Loaded rules: {len(firewall.rules)}")
    print()

    firewall.process(count=10)

    print()
    print("Firewall processing completed.")


if __name__ == "__main__":
    main()