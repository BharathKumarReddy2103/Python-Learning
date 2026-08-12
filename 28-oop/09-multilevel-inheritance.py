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


class FrontendServer(WebServer):

    def serve_frontend(self):
        print(f"Frontend application running on {self.name}")


frontend = FrontendServer("frontend01", "production")

print("Server:", frontend.name)
print("Environment:", frontend.environment)

frontend.start()
frontend.deploy()
frontend.serve_frontend()
frontend.stop()