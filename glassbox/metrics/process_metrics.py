import psutil

class ProcessMetrics:
    @staticmethod
    def top_processes(limit=5):
        processes = []
        for process in psutil.process_iter(
            [
                "pid",
                "name",
                "cpu_percent",
                "memory_percent",
                "status"
            ]
        ):
            try:
                processes.append(
                    {
                        "pid": process.info["pid"],
                        "name": process.info["name"],
                        "cpu": process.info["cpu_percent"],
                        "memory": round(
                            process.info["memory_percent"],
                            2
                        ),
                        "status": process.info["status"]
                    }
                )
            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):
                pass
        
        processes = sorted(
            processes,
            key=lambda x:x["cpu"],
            reverse=True
        )

        return processes[:limit]