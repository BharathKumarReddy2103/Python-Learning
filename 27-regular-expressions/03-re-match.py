import re

text = "ERROR: Kubernetes deployment failed"

result = re.match("ERROR", text)

if result:
    print("Error log detected")
else:
    print("No error at beginning")