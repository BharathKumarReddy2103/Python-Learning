import re

text = "web01:8080"

match = re.search(r"([a-z]+)([0-9]+):([0-9]+)", text)

if match:
    server = match.group(1)
    number = match.group(2)
    port = match.group(3)

    print("Server:", server)
    print("Number:", number)
    print("Port:", port)
else:
    print("No match found")