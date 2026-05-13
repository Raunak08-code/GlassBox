import argparse

from monitoring.monitor_engine import MonitorEngine

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        help = "start"
    )

    args = parser.parse_args()

    if args.command == "start":
        engine = MonitorEngine()
        engine.start()

    else:
        print("Involid command")

if __name__ == "__main__":
    main() 