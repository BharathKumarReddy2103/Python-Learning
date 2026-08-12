import json

with open("server.json", "r") as file:
    server = json.load(file)

print("Name:", server["name"])
print("Environment:", server["environment"])
print("Status:", server["status"])