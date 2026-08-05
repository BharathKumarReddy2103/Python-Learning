inventory = [
    "web01",
    "web02"
]

inventory.extend([
    "db01",
    "redis01"
])

for server in inventory:
    print(server)