pod = {
    "name": "frontend",
    "namespace": "default",
    "status": "Running",
    "node": "worker01"
}

print("Pod Name  :", pod["name"])
print("Namespace :", pod["namespace"])
print("Status    :", pod["status"])
print("Node      :", pod["node"])