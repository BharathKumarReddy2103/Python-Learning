try:
    with open("servers.txt", "r") as file:
        servers = file.read()

    print("Server Inventory:")
    print(servers)

except FileNotFoundError:
    print("Server inventory file not found")

except PermissionError:
    print("Permission denied while accessing server inventory")