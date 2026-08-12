import json

server = {
    "name": "web01",
    "status": "Running"
}

data = json.dumps(server)

print(data)
print(type(data))