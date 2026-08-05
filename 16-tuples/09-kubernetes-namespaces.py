namespaces = (
    "default",
    "kube-system",
    "monitoring",
    "ingress-nginx"
)

for namespace in namespaces:
    print("Namespace:", namespace)