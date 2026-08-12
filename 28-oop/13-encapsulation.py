class Server:

    def __init__(self, name, environment):
        self.name = name
        self._environment = environment
        self.__status = "Stopped"

    def start(self):
        self.__status = "Running"
        print(f"{self.name} server started")

    def stop(self):
        self.__status = "Stopped"
        print(f"{self.name} server stopped")

    def get_status(self):
        return self.__status


server = Server("web01", "production")

print("Server:", server.name)

server.start()

print("Status:", server.get_status())

server.stop()

print("Status:", server.get_status())