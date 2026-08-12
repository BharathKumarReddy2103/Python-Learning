class Server:

    def __init__(self, name, environment):
        self.name = name
        self._environment = environment

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


server = Server("web01", "production")

print("Server:", server.name)
print("Environment:", server.environment)

server.environment = "staging"

print("Updated Environment:", server.environment)