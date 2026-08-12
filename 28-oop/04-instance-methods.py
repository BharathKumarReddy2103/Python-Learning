class Server:

    def __init__(self, name, environment, ip):
        self.name = name
        self.environment = environment
        self.ip = ip

    def start(self):
        print(f"{self.name} server started")

    def stop(self):
        print(f"{self.name} server stopped")

    def restart(self):
        print(f"{self.name} server restarted")

    def health_check(self):
        print(f"{self.name} health check: healthy")


server1 = Server(
    "web01",
    "production",
    "192.168.1.10"
)

server1.start()
server1.health_check()
server1.restart()
server1.stop()