import time



# users = ["guest", "admin", "user1", "user2"]
# found_admin = None

# for user in users:
#     print(f"Checking user: {user}")
#     if user.startswith("admin"):
#         found_admin = user
#         print(f"Admin user found: {found_admin}. Stopping search.")
#         break
    
    
    
    



filenames = ["report.pdf", "data.csv", "db.yaml", "notes.txt"]

for file in filenames:
    print(f"Processing file: {file}")
    if not file.endswith(".yaml"):
        print(f"Skipping non-YAML file: {file}")
        time.sleep(2)
        continue
    print(f"YAML file found: {file}. Processing...")