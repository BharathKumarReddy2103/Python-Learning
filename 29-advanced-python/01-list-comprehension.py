servers = [
    "web01",
    "web02",
    "db01",
    "redis01"
]


server_names = [
    server
    for server in servers
]


print("All Servers:")
print(server_names)


production_servers = [
    server
    for server in servers
    if server.startswith("web")
]


print("Web Servers:")
print(production_servers)