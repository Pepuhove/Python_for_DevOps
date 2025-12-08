import socket

def check_port(host, port, timeout=5):
    """Checks if a TCP port is open on a given host.
    
    Args:
        host (str): The hostname or IP address to check.
        port (int): The TCP port number to check.
        timeout (int, optional): The timeout in seconds. Defaults to 5.
    Returns:
        bool: True if the port is open, False otherwise.
    
    """
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except Exception:
        return False

print(check_port("www.google.com", 443))
print(check_port("www.google.com", 22))
True