import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("API request successful")
    print("Current User URL:", data["current_user_url"])
    print("Repository URL:", data["repository_url"])
else:
    print("API request failed")