import requests

url = "https://api.github.com"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("API request successful")
else:
    print("API request failed")