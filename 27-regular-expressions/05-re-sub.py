import re

text = "server=web01 environment=production"

result = re.sub("production", "staging", text)

print(result)