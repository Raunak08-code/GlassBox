from datetime import datetime

def write_log(message , log_file):
    timestamp = datetime.now()
    log_message = f"[{timestamp}] {message}\n"

    with open(log_file,"a") as file:
        file.write(log_message)