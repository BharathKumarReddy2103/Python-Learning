servers = {
    "web01",
    "db01"
}

servers.discard("web02")

print(servers)