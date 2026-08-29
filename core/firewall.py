from capture.packet_capture import PacketCapture
from core.connection_tracker import ConnectionTracker
from core.logger import FirewallLogger
from core.rule_config import RuleConfigLoader
from core.rule_engine import RuleEngine


class Firewall:
    def __init__(self, interface=None, rule_file="config/rules.json"):
        self.capture = PacketCapture(interface)
        self.engine = RuleEngine()
        self.tracker = ConnectionTracker()
        self.logger = FirewallLogger()

        self.rule_loader = RuleConfigLoader()
        self.rule_file = rule_file
        self.rules = self.rule_loader.load(rule_file)

    def add_rule(self, rule):
        self.rule_loader.add_rule(
            self.rules,
            rule
        )

        self.rule_loader.save(
            self.rule_file,
            self.rules
        )

    def remove_rule(self, index):
        self.rule_loader.remove_rule(
            self.rules,
            index
        )

        self.rule_loader.save(
            self.rule_file,
            self.rules
        )

    def list_rules(self):
        return self.rule_loader.list_rules(
            self.rules
        )

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

            elif state in (
                "ESTABLISHED",
                "ACTIVE",
                "SYN_SENT",
                "SYN_RECEIVED"
            ):
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

            self.logger.log(
                traffic,
                state,
                decision
            )