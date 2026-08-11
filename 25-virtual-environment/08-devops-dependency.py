import requests

print("DevOps automation dependency check")

response = requests.get(
    "https://api.github.com",
    timeout=10
)

print("GitHub API Status:", response.status_code)