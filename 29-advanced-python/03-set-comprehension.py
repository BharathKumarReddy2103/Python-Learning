servers = [
    {"name": "web01", "environment": "production"},
    {"name": "web02", "environment": "staging"},
    {"name": "db01", "environment": "production"},
    {"name": "redis01", "environment": "development"},
]


environments = {
    server["environment"]
    for server in servers
}


print("Environments:")
print(environments)


production_servers = {
    server["name"]
    for server in servers
    if server["environment"] == "production"
}


print("Production Servers:")
print(production_servers)