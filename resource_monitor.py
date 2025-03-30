# resource_monitor.py
import shutil
import psutil

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return f"Disk Usage for {path} - Total: {total//(2**30)}GB, Used: {used//(2**30)}GB, Free: {free//(2**30)}GB"

def check_memory():
    mem = psutil.virtual_memory()
    return f"Memory - Total: {mem.total//(2**20)}MB, Available: {mem.available//(2**20)}MB, Used: {mem.percent}%"
