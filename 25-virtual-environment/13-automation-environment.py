import sys
import os
import requests

print("DevOps Automation Environment")
print("-----------------------------")

print("Python:", sys.version.split()[0])
print("Requests:", requests.__version__)

if os.environ.get("VIRTUAL_ENV"):
    print("Virtual Environment: Active")
else:
    print("Virtual Environment: Not Active")