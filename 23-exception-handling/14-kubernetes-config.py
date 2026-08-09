config = {
    "cluster": "production-eks",
    "namespace": "default",
    "deployment": "frontend"
}

try:
    cluster = config["cluster"]
    namespace = config["namespace"]
    deployment = config["deployment"]

    print("Cluster    :", cluster)
    print("Namespace  :", namespace)
    print("Deployment :", deployment)

except KeyError as error:
    print("Kubernetes configuration missing:", error)