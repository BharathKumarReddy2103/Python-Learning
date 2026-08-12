import json

data = '''
{
    "servers": [
        {
            "name": "web01",
            "ip": "10.0.0.10",
            "role": "frontend",
            "status": "running"
        },
        {
            "name": "web02",
            "ip": "10.0.0.11",
            "role": "frontend",
            "status": "running"
        },
        {
            "name": "db01",
            "ip": "10.0.0.20",
            "role": "database",
            "status": "running"
        }
    ]
}
'''

inventory = json.loads(data)

for server in inventory["servers"]:
    print(
        "Server:",
        server["name"],
        "| IP:",
        server["ip"],
        "| Role:",
        server["role"],
        "| Status:",
        server["status"]
    )