from capture.packet_capture import PacketCapture


def main():
    capture = PacketCapture()
    packets = capture.capture(count=5)

    print(f"Captured packets: {len(packets)}")


if __name__ == "__main__":
    main()