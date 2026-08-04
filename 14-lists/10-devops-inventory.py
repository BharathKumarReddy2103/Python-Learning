inventory = [
    "web01",
    "web02",
    "app01",
    "db01",
    "redis01"
]

print("Total Servers:", len(inventory))

for server in inventory:
    print("Connecting to", server)