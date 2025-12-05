# unique_ports = set([80, 443, 80, 22, 21, 25])
# servers = {"server1", "server2", "server3"}
# print(unique_ports)  # Output: {80, 443, 22, 21, 25}
# print(servers)       # Output: {'server1', 'server2', 'server3'}
# print(22 in unique_ports)
# unique_ports.add(8080)
# unique_ports.remove(21)
# unique_ports.discard(9999)  # Does not raise an error if 9999 is not present
# unique_ports.update([80, 443, 8080])  # Adding multiple elements
# print(unique_ports)  # Output: {80, 443, 22, 21, 25, 8080}

# developers = set(["Alice", "Bob", "Charlie"])
# admins = set(["Bob", "David"])

# print(developers.union(admins))            # Output: {'Alice', 'Bob', 'Charlie', 'David'}
# print(developers.intersection(admins))     # Output: {'Bob'}

print(set([1,2,3,4,3]))