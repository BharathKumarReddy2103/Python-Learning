servers = [
    {"name": "web01", "environment": "production", "status": "running"},
    {"name": "web02", "environment": "staging", "status": "stopped"},
    {"name": "db01", "environment": "production", "status": "running"},
    {"name": "redis01", "environment": "development", "status": "stopped"},
]


production_servers = [
    server["name"]
    for server in servers
    if server["environment"] == "production"
]


print("Production Servers:")
print(production_servers)


server_health = [
    f"{server['name']} - "
    f"{'Healthy' if server['status'] == 'running' else 'Down'}"
    for server in servers
]


print("\nServer Health:")
for health in server_health:
    print(health)