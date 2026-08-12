class Server:

    platform = "Linux"

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment

    @classmethod
    def show_platform(cls):
        print("Default Platform:", cls.platform)

    @classmethod
    def create_production_server(cls, name):
        return cls(name, "production")


Server.show_platform()

server1 = Server.create_production_server("web01")

print("Server:", server1.name)
print("Environment:", server1.environment)