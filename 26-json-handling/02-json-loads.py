import json

data = '{"name": "web01", "status": "Running"}'

server = json.loads(data)

print(server)
print(type(server))