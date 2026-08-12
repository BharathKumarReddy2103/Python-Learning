import re

log = "Kubernetes pod frontend is Running"

result = re.search("frontend", log)

if result:
    print("Pod found")
else:
    print("Pod not found")