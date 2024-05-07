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

def monitor_system():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        print(f"CPU usage: {cpu_percent}%")
        print(f"Memory usage: {memory_percent}%")
        print(f"Disk usage: {disk_percent}%")
        print(f"Total Disk Space: {get_size(shutil.disk_usage('/').total)}")
        print(f"Used Disk Space: {get_size(shutil.disk_usage('/').used)}")
        print(f"Free Disk Space: {get_size(shutil.disk_usage('/').free)}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()