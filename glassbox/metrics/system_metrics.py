import psutil

class SystemMetrics:
    @staticmethod
    def cpu_usage():
        return psutil.cpu_percent(interval=1)
    
    @staticmethod
    def memory_usage():
        return psutil.virtual_memory().percent
    
    @staticmethod
    def disk_usage():
        return psutil.disk_usage("/").percent
    
    @staticmethod
    def disk_free_percentage():
        disk = psutil.disk_usage("/")
        return round(
            100 - disk.percent,
            2
        )
    
    @staticmethod
    def network_stats():
        net = psutil.net_io_counters()
        return {
            "bytes_sent": net.bytes_sent,
            "bytes_recv": net.bytes_recv
        }