with open("kubernetes.log", "r") as file:
    logs = file.read()

if "ERROR" in logs:
    print("Kubernetes Error Found")
else:
    print("Kubernetes Logs Healthy")