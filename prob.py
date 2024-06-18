#problem1.......Develop a script that monitors the health of a Linux system. It should check
#CPU usage, memory usage, disk space, and running processes. If any of
#these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the
#script should send an alert to the console or a log file.

#I used python language...
import psutil

# Define thresholds
CPU_THRESHOLD_PERCENT = 80.0
MEMORY_THRESHOLD_PERCENT = 80.0
DISK_THRESHOLD_PERCENT = 80.0

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD_PERCENT:
        print(f"High CPU usage detected! CPU Usage: {cpu_percent}%")

def check_memory_usage():
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    if mem_percent > MEMORY_THRESHOLD_PERCENT:
        print(f"High memory usage detected! Memory Usage: {mem_percent}%")

def check_disk_usage():
    disk_partitions = psutil.disk_partitions()
    for partition in disk_partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            if usage.percent > DISK_THRESHOLD_PERCENT:
                print(f"High disk usage detected on {partition.mountpoint}! Disk Usage: {usage.percent}%")
        except Exception as e:
            print(f"Error checking disk usage on {partition.mountpoint}: {str(e)}")

def check_running_processes():
    # Example: Check for specific processes or total number of processes
    num_processes = len(psutil.pids())
    print(f"Total number of running processes: {num_processes}")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
