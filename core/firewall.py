from capture.packet_capture import PacketCapture
from core.connection_tracker import ConnectionTracker
from core.rule_engine import RuleEngine


class Firewall:
    def __init__(self, interface=None):
        self.capture = PacketCapture(interface)
        self.engine = RuleEngine()
        self.tracker = ConnectionTracker()
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def process(self, count=10):
        traffic_list = self.capture.capture(count)

        for traffic in traffic_list:
            if traffic is None:
                continue

            state = self.tracker.get_state(traffic)
            flags = traffic.tcp_flags or ""

            if traffic.protocol == "TCP" and ("F" in flags or "R" in flags):
                if state is not None:
                    decision = "ALLOW"
                    state = self.tracker.update(traffic)
                else:
                    decision = self.engine.evaluate(
                        self.rules,
                        traffic
                    )

            elif state in ("ESTABLISHED", "ACTIVE", "SYN_SENT", "SYN_RECEIVED"):
                decision = "ALLOW"

                if traffic.protocol == "TCP":
                    state = self.tracker.update(traffic)

            else:
                decision = self.engine.evaluate(
                    self.rules,
                    traffic
                )

                if decision == "ALLOW":
                    state = self.tracker.update(traffic)

            print(traffic)
            print("State:", state or "NEW")
            print("Decision:", decision)