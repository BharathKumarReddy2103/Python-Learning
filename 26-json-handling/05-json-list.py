import json

data = '''
{
    "servers": [
        "web01",
        "web02",
        "db01"
    ]
}
'''

inventory = json.loads(data)

servers = inventory["servers"]

print(servers)

for server in servers:
    print("Server:", server)