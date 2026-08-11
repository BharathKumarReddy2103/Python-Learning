def check_cpu(usage):
    if usage >= 80:
        print("High CPU Usage")
    else:
        print("CPU Usage Normal")


def check_memory(usage):
    if usage >= 80:
        print("High Memory Usage")
    else:
        print("Memory Usage Normal")