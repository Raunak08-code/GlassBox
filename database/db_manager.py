import psycopg2
import time
import os 

class DatabaseManager:
    def __init__(self):
        while True:
            try:
                self.connection = psycopg2.connect(
                    host = os.getenv(
                        "DB_HOST",
                        "localhost"
                    ),
                    port=5432,
                    database = 'observability_platform',
                    user = 'postgres',
                    password = "postgres"
                )
                self.cursor = (
                    self.connection.cursor()
                )
                print("Connected to postgres")
                break
            except psycopg2.OperationalError:
                print(
                    "postgreSQL not ready..."
                    "retring in 5 seconds"
                )
                time.sleep(5)
    
    def insert_system_metrics(self,cpu,memory,disk,network):
        query = """
        INSERT INTO system_metrics(cpu_usage, memory_usage,disk_usage,bytes_sent,bytes_received)
        VALUES (%s,%s,%s,%s,%s)        
        """
        values = (cpu,memory,disk,network["bytes_sent"],network["bytes_recv"])

        self.cursor.execute(query,values)
        self.connection.commit()