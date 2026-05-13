from rich.console import Group
from rich.table import Table
from metrics.process_metrics import ProcessMetrics
from metrics.system_metrics import SystemMetrics
from docker_monitoring.container_metrics import ContainerMetrics

class Dashboard:
    def __init__(self):
        self.console = Group()
        
    
    
    def build_dashboard(
        self,
        cpu,
        memory,
        disk,
        disk_free,
        network
    ):
        system_table = Table(
            title="System Observability Dashboard"
        )
        
        system_table.add_column("Metric")
        system_table.add_column("Value")

        disk_free = SystemMetrics.disk_free_percentage()

        print(type(disk_free))
        print(disk_free)
        print(type(disk))
        print(disk)

        system_table.add_row("CPU Usage",f"{cpu}%")
        system_table.add_row("Memory Usage",f"{memory}%")
        system_table.add_row("Disk Used", f"{disk}%")
        system_table.add_row("Disk Free",f"{disk_free}%")
        system_table.add_row(
            "Bytes Sent",
            str(network["bytes_sent"])
        )
        system_table.add_row(
            "Bytes Receives",
            str(network["bytes_recv"])
        ) 

    # table 2 prcess table...
        process_table = Table(
            title="Top Processes"
        )

        process_table.add_column("PID")
        process_table.add_column("NAME")
        process_table.add_column("CPU %")
        process_table.add_column("MEMORY %")
        process_table.add_column("STATUS")

        processes = (
            ProcessMetrics.top_processes()
        )

        for process in processes:
            process_table.add_row (
                str(process["pid"]),
                process["name"],
                str(process["cpu"]),
                str(process["memory"]),
                process["status"]
            )

    # container table added
        container_table = Table(
            title="Docker Container"
        )
        container_table.add_column("NAME")
        container_table.add_column("STATUS")
        container_table.add_column("CPU %")
        container_table.add_column("MEMORY %")

        container_mertrics = ContainerMetrics()
        containers = (
            container_mertrics.container_stats()
        )
        for container in containers:
            container_table.add_row(
                container["name"],
                container["status"],
                str(container["cpu_percent"]),
                str(container["memory_mb"])
            )

        return Group(
            system_table,
            process_table,
            container_table 
        )