import os
import time
import psutil
import shutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def cpu_usage():
    return str(psutil.cpu_percent()) + "%"

def memory_usage():
    svmem = psutil.virtual_memory()
    return f"Total: {get_size(svmem.total)}, Available: {get_size(svmem.available)}, Used: {get_size(svmem.used)}, Percentage: {svmem.percent}%"

def disk_usage():
    partition_usage = psutil.disk_usage("/")
    return f"Total: {get_size(partition_usage.total)}, Used: {get_size(partition_usage.used)}, Free: {get_size(partition_usage.free)}, Percentage: {partition_usage.percent}%"

def network_usage():
    net_io = psutil.net_io_counters()
    return f"Bytes Sent: {get_size(net_io.bytes_sent)}, Bytes Received: {get_size(net_io.bytes_recv)}"


def monitor_system():
    while True:
        cpu_usage_info = cpu_usage()
        memory_usage_info = memory_usage()
        disk_usage_info = disk_usage()
        network_usage_info = network_usage()

        print(f"CPU usage: {cpu_usage_info}%")
        print(f"Memory usage: {memory_usage_info}%")
        print(f"Disk usage: {disk_usage_info}%")
        print(f"network usage: {network_usage_info}%")
        print(f"Total Disk Space: {get_size(shutil.disk_usage('/').total)}")
        print(f"Used Disk Space: {get_size(shutil.disk_usage('/').used)}")
        print(f"Free Disk Space: {get_size(shutil.disk_usage('/').free)}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()