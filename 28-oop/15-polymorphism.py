class Server:

    def start(self):
        print("Server started")

    def stop(self):
        print("Server stopped")


class WebServer(Server):

    def start(self):
        print("Web server started")


class DatabaseServer(Server):

    def start(self):
        print("Database server started")


class CacheServer(Server):

    def start(self):
        print("Cache server started")


servers = [
    WebServer(),
    DatabaseServer(),
    CacheServer()
]


for server in servers:
    server.start()
    server.stop()