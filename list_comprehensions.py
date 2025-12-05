# old_items = [1,2,3,4,5]

# doubled_items = [item * 2 for item in old_items]
# print(doubled_items)  # Output: [2, 4, 6, 8, 10]

# servers = ["web01", "web02", "db01", "db02"]

# upper_cased_servers = [server.upper() for server in servers ]
# print(upper_cased_servers)  # Output: ['WEB01', 'WEB02', 'DB01', 'DB02']

# squared_items = list(map(lambda item: item ** 2 , old_items))
# print(squared_items)  # Output: [1, 4, 9, 16, 25]




servers_cpu_usage = {"web01": 55, "web02": 35, "db01": 75, "db02": 85}

results = [f"Alert!! High CPU usage: {usage}" if usage > 70 else f"Normal CPU usage: {usage}" for server, usage in servers_cpu_usage.items()] 
print(results)

