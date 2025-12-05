import math

server_name = "Server-01"
disk_total_gb = 500  # in GB
cpu_cores = 4
memory_gb = 8.0  # in GB
disk_used_gb = 350  # in GB

disk_usage_percentage = (disk_used_gb / disk_total_gb) * 100
print(f"Disk usage for {server_name}: {disk_usage_percentage:.2f}%")
print(f"CPU_cores: {cpu_cores}\nMemory: {memory_gb}\nDisk Total: {disk_total_gb}GB")