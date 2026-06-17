import time
from glassbox.logs.logging_manager import LoggingManager
from glassbox.alert.alert_manager import AlertManager
from glassbox.metrics.system_metrics import SystemMetrics
from glassbox.dashboard.live_dashboard import Dashboard
from glassbox.exporters.prometheus_exporter import PrometheusExporter
from glassbox.database.db_manager import DatabaseManager
from rich.live import Live

class MonitorEngine:

# constructor...
    def __init__(self,interval=5):
        self.interval = interval
        self.logger = LoggingManager().get_logger()
        self.dashboard = Dashboard() 
        PrometheusExporter.start()
        self.db = DatabaseManager()

# start monitoring ...
    def start(self):
        try:
            self.logger.info("Monitoring Engine Started...\n")

            # live dashboard updation..
            with Live(
                refresh_per_second=1,
                screen=True
            ) as live:
                while True:
                    cpu = SystemMetrics.cpu_usage()
                    memory = SystemMetrics.memory_usage()
                    disk = SystemMetrics.disk_usage()
                    disk_free = SystemMetrics.disk_free_percentage()
                    network = SystemMetrics.network_stats()
                    print(type(disk_free))
                    print(disk_free)
                    layout = (
                        self.dashboard.build_dashboard(
                            cpu, 
                            memory,
                            disk,
                            disk_free, 
                            network)
                    )
        
                    # prometheus monitoring data
                    self.logger.info(
                         f"Prometheus Update: CPU={cpu}, MEM={memory}, DISK={disk}"
                    )
                    PrometheusExporter.update( cpu,memory,disk)
                
                    # database intregation...
                    self.db.insert_system_metrics(cpu,memory,disk,network)

                    # alert system intregretates...
                    cpu_alert = AlertManager.cpu_alert(cpu)
                    if cpu_alert:
                        self.logger.warning(cpu_alert)

                    memory_alert = AlertManager.memory_alert(memory)
                    if memory_alert:
                        self.logger.warning(memory_alert)

                    disk_alert = AlertManager.disk_alert(disk)
                    if disk_alert:
                        self.logger.warning(disk_alert)

                
                    live.update(layout)
                    time.sleep(self.interval) 
        except KeyboardInterrupt:
            self.logger.info("\n Monitoring Engine Ends Gracefully...")