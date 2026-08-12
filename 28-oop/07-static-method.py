class Server:

    @staticmethod
    def validate_ip(ip):
        parts = ip.split(".")

        if len(parts) == 4:
            print(f"Valid IP format: {ip}")
        else:
            print(f"Invalid IP format: {ip}")


Server.validate_ip("192.168.1.10")
Server.validate_ip("192.168.1")