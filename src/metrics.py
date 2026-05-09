import psutil

def get_cpu_usages():
    return psutil.cpu_percent(interval=1)

def get_memory_usages():
    return psutil.virtual_memory().percent