servers = [
    "web01",
    "web02",
    "app01",
    "db01",
    "redis01"
]

with open("inventory.txt", "w") as file:
    for server in servers:
        file.write(server + "\n")

print("Inventory created")