import docker


class ContainerMetrics:
    def __init__(self):
        self.client = docker.from_env()

    def container_stats(self):
        containers = self.client.containers.list()
        container_data = []
        for container in containers:
            try:
                stats = container.stats(
                    stream=False
                )

                memory_usage = (
                    stats["memory_stats"]
                    ["usage"]
                    / (1024 * 1024)
                )

                cpu_delta = (
                    stats["cpu_stats"]
                    ["cpu_usage"]
                    ["total_usage"]
                    -
                    stats["precpu_stats"]
                    ["cpu_usage"]
                    ["total_usage"]
                )

                system_delta = (
                    stats["cpu_stats"]
                    ["system_cpu_usage"]
                    -
                    stats["precpu_stats"]
                    ["system_cpu_usage"]
                )

                cpu_percent = 0.0
                if system_delta > 0:
                    cpu_percent = (
                        cpu_delta /
                        system_delta
                    ) * 100

                container_data.append({
                    "name": container.name,
                    "status": container.status,
                    "memory_mb": round(
                        memory_usage,
                        2
                    ),
                    "cpu_percent": round(
                        cpu_percent,
                        2
                    )
                })
            except Exception:
                pass
        return container_data