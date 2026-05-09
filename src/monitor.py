import csv
import time
import os
from datetime import datetime

from config_loader import load_config
from logger import write_log
from metrics import get_cpu_usages,get_memory_usages

def initialize_csv(csv_file):
    try:
        with open(csv_file,"x",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "cpu_usage",
                "memory_usage"
            ])
    except FileExistsError:
        pass

def write_csv(cpu,memory,csv_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(csv_file,"a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            cpu,
            memory
        ])

def start_monitoring():
    try:
        config = load_config()

        interval = config["interval"]
        threshold = config["cpu_threshold"]
        log_file = config["log_file"]
        csv_file = config["csv_file"]

        os.makedirs("logs",exist_ok=True)

        initialize_csv(csv_file)

        cpu = get_cpu_usages()
        memory = get_memory_usages()

        print("System Monitoring started ...\n")
        write_log("monitoring initlized", log_file)
    
        while True:
            cpu = get_cpu_usages()
            memory = get_memory_usages()

            print(f"CPU: {cpu}% | MEMORY; {memory}%")
            write_csv(cpu,memory,csv_file)
            write_log("monitoring runnning",log_file)

            if cpu > threshold:
                Warning_message = f"WARNING: CPU usages crossed {threshold}% -> current CPU: {cpu}%"
                print(Warning_message)
                write_log(Warning_message,log_file)
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n Monitoring stopped successfully...")
        write_log("Monitoring stopped",log_file)
    
    except Exception as error:
        error_message = f"CRITICAL ERROR: {str(error)}"
        print(error_message)
        write_log(error_message,log_file)