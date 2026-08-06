server = {
    "name": "web01",
    "ip": "10.0.0.10",
    "status": "Running"
}

for key in server:
    print(key, ":", server[key])