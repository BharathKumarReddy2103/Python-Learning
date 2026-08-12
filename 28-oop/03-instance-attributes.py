class Server:

    def __init__(self, name, environment, ip):
        self.name = name
        self.environment = environment
        self.ip = ip


server1 = Server(
    "web01",
    "production",
    "192.168.1.10"
)

server2 = Server(
    "web02",
    "development",
    "192.168.1.11"
)


print("Server:", server1.name)
print("Environment:", server1.environment)
print("IP:", server1.ip)

print()

print("Server:", server2.name)
print("Environment:", server2.environment)
print("IP:", server2.ip)