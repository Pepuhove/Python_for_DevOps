servers = ["web01", "web02", "db01", "db02", "cache01"]

# for server in servers:
#     # print(f"Sever_name: {server}")
#     if server.startswith("db"):
#         server
#         print("Database server found, stopping the listing.")
#         print(server)
#         break

[server for server in servers if server.startswith("db")]
print(f"There are {len([server for server in servers if server.startswith('db')])} database servers.")
print(f"Database servers are: {[server for server in servers if server.startswith('db')]}")

ports = [80, 443, 22, 3306, 6379]
ports.insert(2, 8080)
ports.append(5432)

print(ports)
print(len(ports))

for port in ports:
    if str(port).startswith("8") and str(port).endswith("0") and len(str(port)) == 2:
        print(f"Port {port} is used for HTTP traffic.")
        
deployment_targets = ["us-east-1", "us-west-2", "eu-central-1", "ap-southeast-1"]

print(deployment_targets[0])