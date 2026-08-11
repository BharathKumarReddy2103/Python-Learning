def check_server(server):
    print("Checking server:", server)


def check_disk_usage(usage):
    if usage >= 80:
        print("Warning: High disk usage")
    else:
        print("Disk usage normal")