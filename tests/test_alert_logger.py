from core.alert_logger import AlertLogger


def main():
    logger = AlertLogger()

    alert = {
        "type": "TEST_ALERT",
        "severity": "HIGH",
        "message": "Test alert generated successfully",
        "count": 1
    }

    logger.log(alert)

    print("Alert written successfully.")


if __name__ == "__main__":
    main()