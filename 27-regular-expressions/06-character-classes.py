import re

text = "Servers: web01 web02 db01"

servers = re.findall(r"[a-z]+[0-9]+", text)

print(servers)