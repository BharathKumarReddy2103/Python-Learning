class Server:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment

    def start(self):
        print(f"{self.name} server started")

    def stop(self):
        print(f"{self.name} server stopped")


class WebServer(Server):

    def start(self):
        super().start()
        print(f"{self.name} web server configuration loaded")


web = WebServer("web01", "production")

print("Server:", web.name)
print("Environment:", web.environment)

web.start()
web.stop()