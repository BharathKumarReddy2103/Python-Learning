servers = [
    {"name": "web01", "status": "running"},
    {"name": "web02", "status": "stopped"},
    {"name": "db01", "status": "running"},
]


server_status = {
    server["name"]: server["status"]
    for server in servers
}


print("Server Status:")
print(server_status)


running_servers = {
    server["name"]: server["status"]
    for server in servers
    if server["status"] == "running"
}


print("Running Servers:")
print(running_servers)