server = {
    "name": "web01",
    "status": "Running"
}

print(server.get("name"))
print(server.get("status"))
print(server.get("region"))
print(server.get("region", "Not Found"))