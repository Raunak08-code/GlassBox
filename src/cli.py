import argparse

from monitor import start_monitoring

def main():
    parser = argparse.ArgumentParser(
        description="System-Monitoring-CLI-Tool"
    )
    parser.add_argument(
        "command",
        help = "start | status"
    )

    args = parser.parse_args()
    if args.command == "start":
        start_monitoring()
    elif args.command == "status":
        print("System Monitoring Tool is Ready")
    else:
        print("Involid command")

if __name__ == "__main__":
    main()