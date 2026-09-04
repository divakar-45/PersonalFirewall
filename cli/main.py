import argparse

from core.firewall import Firewall
from core.monitor_engine import MonitorEngine
from core.dashboard import SecurityDashboard


def firewall_command(args):
    firewall = Firewall()

    print("=" * 50)
    print("             PERSONAL FIREWALL")
    print("=" * 50)
    print()
    print(f"Loaded rules: {len(firewall.rules)}")
    print()

    firewall.process(count=args.count)

    print()
    print("Firewall processing completed.")


def monitor_command(args):
    monitor = MonitorEngine(
        log_file=args.log_file,
        poll_interval=args.interval
    )

    monitor.run()


def dashboard_command(args):
    dashboard = SecurityDashboard()
    dashboard.display()


def main():
    parser = argparse.ArgumentParser(
        description="Personal Firewall Security CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    firewall_parser = subparsers.add_parser(
        "firewall",
        help="Capture and process network traffic"
    )

    firewall_parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=10,
        help="Number of packets to process"
    )

    firewall_parser.set_defaults(
        func=firewall_command
    )

    monitor_parser = subparsers.add_parser(
        "monitor",
        help="Start the security monitoring engine"
    )

    monitor_parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=2,
        help="Monitoring interval in seconds"
    )

    monitor_parser.add_argument(
        "-l",
        "--log-file",
        default="logs/firewall.log",
        help="Firewall log file"
    )

    monitor_parser.set_defaults(
        func=monitor_command
    )

    dashboard_parser = subparsers.add_parser(
        "dashboard",
        help="Display firewall security dashboard"
    )

    dashboard_parser.set_defaults(
        func=dashboard_command
    )

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()