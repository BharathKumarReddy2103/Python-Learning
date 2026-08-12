import json

server = {
    "name": "web01",
    "environment": "production",
    "status": "Running",
    "platform": "Kubernetes"
}

with open("server-output.json", "w") as file:
    json.dump(server, file, indent=4)

print("JSON file created")