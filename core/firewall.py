from config.settings import DEFAULT_POLICY
from backends.base import FirewallBackend


class Firewall:
    def __init__(self, backend: FirewallBackend):
        self.enabled = False
        self.default_policy = DEFAULT_POLICY
        self.backend = backend

    def enable(self):
        self.backend.enable()
        self.enabled = True

    def disable(self):
        self.backend.disable()
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def get_default_policy(self):
        return self.default_policy