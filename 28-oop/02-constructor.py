class Server:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment


server1 = Server("web01", "production")
server2 = Server("web02", "production")

print("Server:", server1.name)
print("Environment:", server1.environment)

print("Server:", server2.name)
print("Environment:", server2.environment)