# server_status = "running"

# if server_status == "running":
#     print("The server is up and running.")
    
# servers = ["web01", "web02", "db01", "db02"]
# error_message = ""
# default_config = {}

# if servers:
#     print(f"Processing {len(servers)} servers.")
# if error_message:
#     print(f"Something went wrong: {error_message}")
# if not default_config:
#     print("Default config not available, please provide the configuration values.")


# cpu_usage = 85.0

# if cpu_usage > 90.0:
#     print("ALERT: High CPU usage detected!")
# else:
#     print("CPU usage is within normal limits.")


# http_status_code = 404

# if http_status_code == 200:
#     print("Status OK.")
# elif http_status_code == 404:
#     print("Error: Resource not found.")
# elif http_status_code == 500:
#     print("Error: Internal server error.")
# else:
#     print(f"Unexpected status code: {http_status_code}.")


def process_data_guarded(data):
    if not data:
        print("No data to provided.")
    elif not isinstance(data, list):
        print(f"Invalid value type for 'data'. Provided {type(data)} Please provide a list.")
    else:
        print(f"Processing {len(data)} data items.")
        print("Data processed successfully.")
process_data_guarded(None)
process_data_guarded([])
process_data_guarded("abc")
process_data_guarded([1, 2, 3])