class Logger:

    def log(self, message):
        print(f"LOG: {message}")


class Server:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        self.logger = Logger()

    def start(self):
        self.logger.log(f"{self.name} server started")

    def stop(self):
        self.logger.log(f"{self.name} server stopped")


server = Server("web01", "production")

print("Server:", server.name)
print("Environment:", server.environment)

server.start()
server.stop()