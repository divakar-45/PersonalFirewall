from backends.mock import MockFirewallBackend
from core.firewall import Firewall


def main():
    backend = MockFirewallBackend()
    firewall = Firewall(backend)

    print(f"Firewall enabled: {firewall.is_enabled()}")
    print(f"Default policy: {firewall.get_default_policy()}")

    firewall.enable()
    print(f"Firewall enabled: {firewall.is_enabled()}")

    firewall.disable()
    print(f"Firewall enabled: {firewall.is_enabled()}")


if __name__ == "__main__":
    main()