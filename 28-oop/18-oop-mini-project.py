from abc import ABC, abstractmethod


class Logger:

    def log(self, message):
        print(f"LOG: {message}")


class Server:

    platform = "Linux"

    def __init__(self, name, environment, ip):
        self.name = name
        self._environment = environment
        self.ip = ip
        self.__status = "Stopped"
        self.logger = Logger()

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, value):

        valid_environments = [
            "development",
            "staging",
            "production"
        ]

        if value not in valid_environments:
            raise ValueError("Invalid environment")

        self._environment = value

    def start(self):
        self.__status = "Running"
        self.logger.log(f"{self.name} server started")

    def stop(self):
        self.__status = "Stopped"
        self.logger.log(f"{self.name} server stopped")

    def status(self):
        return self.__status


class WebServer(Server):

    def start(self):
        super().start()
        self.logger.log(f"{self.name} web server started")


class DatabaseServer(Server):

    def start(self):
        super().start()
        self.logger.log(f"{self.name} database server started")


class Deployment(ABC):

    @abstractmethod
    def deploy(self, server):
        pass


class WebDeployment(Deployment):

    def deploy(self, server):
        print(f"Deploying web application on {server.name}")


class DatabaseDeployment(Deployment):

    def deploy(self, server):
        print(f"Deploying database configuration on {server.name}")


web_server = WebServer(
    "web01",
    "production",
    "192.168.1.10"
)

db_server = DatabaseServer(
    "db01",
    "production",
    "192.168.1.20"
)


print("=== Server Information ===")

print(
    f"Server: {web_server.name} | "
    f"Environment: {web_server.environment} | "
    f"IP: {web_server.ip}"
)

print(
    f"Server: {db_server.name} | "
    f"Environment: {db_server.environment} | "
    f"IP: {db_server.ip}"
)


print("\n=== Server Operations ===")

servers = [
    web_server,
    db_server
]

for server in servers:
    server.start()
    print(f"Status: {server.status()}")


print("\n=== Deployment ===")

deployments = [
    WebDeployment(),
    DatabaseDeployment()
]

for deployment, server in zip(deployments, servers):
    deployment.deploy(server)


print("\n=== Environment Update ===")

web_server.environment = "staging"

print(
    f"{web_server.name} environment changed to "
    f"{web_server.environment}"
)


print("\n=== Server Shutdown ===")

for server in servers:
    server.stop()
    print(f"Status: {server.status()}")