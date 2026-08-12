class Monitoring:

    def check_health(self):
        print(f"{self.name} health check: healthy")


class Logging:

    def collect_logs(self):
        print(f"Collecting logs from {self.name}")


class Server(Monitoring, Logging):

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment

    def start(self):
        print(f"{self.name} server started")


server = Server("web01", "production")

print("Server:", server.name)
print("Environment:", server.environment)

server.start()
server.check_health()
server.collect_logs()