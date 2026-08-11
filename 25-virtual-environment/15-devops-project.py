import sys
import requests

print("================================")
print(" DevOps Automation Environment")
print("================================")

print("Python Version :", sys.version.split()[0])
print("Requests       :", requests.__version__)

response = requests.get(
    "https://api.github.com",
    timeout=10
)

if response.status_code == 200:
    print("GitHub API     : Available")
else:
    print("GitHub API     : Unavailable")

print("Environment    : Ready")