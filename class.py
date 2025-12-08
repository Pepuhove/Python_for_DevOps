class ServiceMonitor:
    """Provides service checks for a single service."""
    def __init__(self, service_name, port):
        """Initializes the monitor or a specific service.
        
        Args:
            service_name (str): The name of the service to monitor.
            port (int): The port number the service is running on.
        """
        print(f"Initializing monitor for service: {service_name} on port: {port}")
        self.service_name = service_name
        self.port = port
        self.is_alive = False
        
nginx_monitor = ServiceMonitor("nginx", 80)
print(type(nginx_monitor))