class Server:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment

    def start(self):
        print(f"{self.name} server started")

    def stop(self):
        print(f"{self.name} server stopped")


class WebServer(Server):

    def deploy(self):
        print(f"Application deployed on {self.name}")


web01 = WebServer("web01", "production")

print("Server:", web01.name)
print("Environment:", web01.environment)

web01.start()
web01.deploy()
web01.stop()