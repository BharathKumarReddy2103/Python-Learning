servers = [
    "web01\n",
    "web02\n",
    "app01\n",
    "db01\n",
    "redis01\n"
]

with open("server-inventory.txt", "w") as file:
    file.writelines(servers)

print("Server inventory created")