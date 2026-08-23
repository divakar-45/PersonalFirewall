from capture.packet_capture import PacketCapture
from cli.formatter import format_traffic


def main():
    capture = PacketCapture()
    traffic = capture.capture(5)

    for item in traffic:
        print(format_traffic(item))


if __name__ == "__main__":
    main()