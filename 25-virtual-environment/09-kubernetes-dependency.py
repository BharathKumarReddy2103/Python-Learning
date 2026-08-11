import requests

print("Kubernetes automation environment")

response = requests.get(
    "https://kubernetes.io",
    timeout=10
)

print("Kubernetes website status:", response.status_code)