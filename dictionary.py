# my_dic = {'a':1, 'b':2, 'c':4}

# print(my_dic.keys())
# print(my_dic.values())
# print(my_dic.items())
# print(len(my_dic))

# default_tags = {
#     "Environment": "Production",
#     "Owner": "Admin",
# }

# custom_tags = {
#     "Project": "Alpha"
# }

# merged_tags = default_tags | custom_tags
# print(merged_tags)

server_infor = {
    "id": "web01",
    "ip_address": "192.168.1.1",
    "instance_type": "t2.micro",
    "state": "running",
    "tags": {
        "Environment": "Production",
        "Owner": "Admin",
    }
}

print(f"Server state: {server_infor.get("state")}")
print(server_infor.get("tags")["Environment"])
for key, value in server_infor.items():
    print(f"- {key}: {value}")