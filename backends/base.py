from abc import ABC, abstractmethod


class FirewallBackend(ABC):
    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def apply_rule(self, rule):
        pass

    @abstractmethod
    def remove_rule(self, rule):
        pass