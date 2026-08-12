import re

text = "Server IP: 192.168.1.100"

pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

match = re.search(pattern, text)

if match:
    print("IP Address:", match.group())
else:
    print("IP address not found")