from backends.base import FirewallBackend


class MockFirewallBackend(FirewallBackend):
    def enable(self):
        print("Backend enabled")

    def disable(self):
        print("Backend disabled")

    def apply_rule(self, rule):
        print(f"Rule applied: {rule}")

    def remove_rule(self, rule):
        print(f"Rule removed: {rule}")