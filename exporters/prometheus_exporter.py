from prometheus_client import start_http_server, Gauge

cpu_metric = Gauge(
    "system_cpu_usage",
    "CPU Usage"
)

memory_metric = Gauge(
    "system_memory_usage",
    "memory Usage"
)

disk_metric = Gauge(
    "system_disk_usage",
    "Disk Usage"
)

class PrometheusExporter:
    @staticmethod
    def start ():
        start_http_server(8000)

    @staticmethod
    def update(cpu,memory,disk):
        cpu_metric.set(cpu)
        memory_metric.set(memory)
        disk_metric.set(disk)
