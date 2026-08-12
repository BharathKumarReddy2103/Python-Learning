class Server:

    platform = "Linux"

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
    "production",
    "192.168.1.11"
)

server3 = Server(
    "db01",
    "production",
    "192.168.1.20"
)


print("Server:", server1.name)
print("Platform:", server1.platform)

print()

print("Server:", server2.name)
print("Platform:", server2.platform)

print()

print("Server:", server3.name)
print("Platform:", server3.platform)