
import argparse

from core.firewall import Firewall
from core.monitor_engine import MonitorEngine
from core.dashboard import SecurityDashboard


def start_command(args):
    firewall = Firewall()

    print("=" * 50)
    print("             PERSONAL FIREWALL")
    print("=" * 50)
    print()
    print(f"Loaded rules: {len(firewall.rules)}")
    print(f"Packets to process: {args.count}")
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


def status_command(args):
    firewall = Firewall()

    print("=" * 50)
    print("             FIREWALL STATUS")
    print("=" * 50)
    print()
    print("Status: READY")
    print(f"Loaded rules: {len(firewall.rules)}")
    print("Monitoring engine: AVAILABLE")
    print("Security dashboard: AVAILABLE")
    print("Traffic logging: ENABLED")
    print()


def main():
    parser = argparse.ArgumentParser(
        prog="firewall",
        description="Personal Firewall Security CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    start_parser = subparsers.add_parser(
        "start",
        help="Capture and process network traffic"
    )

    start_parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=10,
        help="Number of packets to process"
    )

    start_parser.set_defaults(
        func=start_command
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

    status_parser = subparsers.add_parser(
        "status",
        help="Display firewall system status"
    )

    status_parser.set_defaults(
        func=status_command
    )

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
