server = {
    "hostname": "web01",
    "ip": "10.0.0.10",
    "os": "Ubuntu",
    "cpu": 4,
    "memory": "8GB",
    "environment": "Production"
}

for key in server:
    print(key, ":", server[key])