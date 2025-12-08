# def greet_user(name):
#     """
#     Greets the user with a personalized message.

#     Parameters:
#     name (str): The name of the user.

#     Returns:
#     str: A greeting message.
#     """
#     return f"Hello, {name}! Welcome back!"
# greet_user("Alice")
# print(greet_user("Alice"))



import random
# def random_number(min_value, max_value):
#     """
#     Generates a random integer between min_value and max_value.

#     Parameters/arguments:
#     min_value (int): The minimum value of the range.
#     max_value (int): The maximum value of the range.

#     Returns:
#     int: A random integer within the specified range.
#     """
    
#     return random.randint(min_value, max_value)

# generated_numbers = random_number(1, 10)
# print(f"Generated number: {generated_numbers}")



# def check_service_status(service_name, expected_status):
#     """
#     Checks the status of a given service.

#     Parameters:
#     service_name (str): The name of the service to check.

#     Returns:
#     str: The status of the service.
#     """
#     # Simulated service status check
#     services = {
#         "database": "running",
#         "webserver": "stopped",
#         "cache": "running"
#     }
#     return services.get(service_name, "unknown service")


def check_service_status(service_name, expected_status):
    print(f"Checking {service_name} for {expected_status}...")
    return True

check_service_status("nginx", "running")
