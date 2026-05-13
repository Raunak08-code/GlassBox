class AlertManager:
    @staticmethod
    def cpu_alert(cpu):
        if cpu > 80:
            return (
                f"HIGH CPU USAGE ALERT: {cpu}%"
            )
        return None
    
    @staticmethod
    def memory_alert(memory):
        if memory > 85:
            return (
                f"HIGH MEMORY USAGE ALERT: "
                f"{memory}%"
            )
        return None
    
    @staticmethod
    def disk_alert(disk):
        space_left = 100-disk 
        if space_left < 10:
            return (
                f"LOW DISK SPACE, ONLY {space_left}% SPACE AVAILABLE"
            )
        return None