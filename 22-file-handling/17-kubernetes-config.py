config = [
    "namespace=production\n",
    "replicas=3\n",
    "image=nginx:1.27\n",
    "environment=production\n"
]

with open("kubernetes-config.txt", "w") as file:
    file.writelines(config)

print("Kubernetes configuration created")