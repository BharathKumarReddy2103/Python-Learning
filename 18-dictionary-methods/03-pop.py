server = {
    "name": "web01",
    "status": "Running",
    "ip": "10.0.0.10"
}

server.pop("status")

print(server)