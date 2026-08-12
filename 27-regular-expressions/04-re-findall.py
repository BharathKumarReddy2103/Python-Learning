import re

text = "web01 web02 db01"

servers = re.findall(r"\w+", text)

print(servers)