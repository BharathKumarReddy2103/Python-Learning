import json

data = '''
{
    "name": "web01",
    "port": 8080,
    "healthy": true,
    "backup": null
}
'''

server = json.loads(data)

print("Name:", server["name"])
print("Port:", server["port"])
print("Healthy:", server["healthy"])
print("Backup:", server["backup"])

print(type(server["name"]))
print(type(server["port"]))
print(type(server["healthy"]))
print(type(server["backup"]))