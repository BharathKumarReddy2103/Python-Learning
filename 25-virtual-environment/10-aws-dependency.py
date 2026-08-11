import requests

print("AWS automation dependency check")

response = requests.get(
    "https://aws.amazon.com",
    timeout=10
)

print("AWS website status:", response.status_code)