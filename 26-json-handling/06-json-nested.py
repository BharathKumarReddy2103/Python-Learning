import json

data = '''
{
    "server": {
        "name": "web01",
        "network": {
            "ip": "10.0.0.10",
            "port": 8080
        }
    }
}
'''

server = json.loads(data)

print("Server:", server["server"]["name"])
print("IP:", server["server"]["network"]["ip"])
print("Port:", server["server"]["network"]["port"])