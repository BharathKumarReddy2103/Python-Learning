class Server:

    def start(self):
        print(f"{self.name} server started")

    def stop(self):
        print(f"{self.name} server stopped")


class WebServer(Server):

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} web server started")


class DatabaseServer(Server):

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} database server started")


web = WebServer("web01")
database = DatabaseServer("db01")

web.start()
database.start()

web.stop()
database.stop()