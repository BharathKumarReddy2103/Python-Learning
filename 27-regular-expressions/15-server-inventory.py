import re

inventory = """
web01 192.168.1.10
web02 192.168.1.11
db01 192.168.1.20
"""

pattern = r"([a-z]+[0-9]+)\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})"

servers = re.findall(pattern, inventory)

for server, ip in servers:
    print("Server:", server)
    print("IP:", ip)