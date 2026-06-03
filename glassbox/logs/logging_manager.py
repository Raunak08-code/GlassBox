import logging
import os

class LoggingManager:
    def __init__(self):
        os.makedirs("logs",exist_ok=True)
        self.logger = logging.getLogger("observablityPlatform")
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s"
        )

        file_handler = logging.FileHandler(
            "glassbox/logs/system.log",
             encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger