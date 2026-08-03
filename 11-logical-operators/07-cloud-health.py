cpu = int(input("CPU Usage: "))
memory = int(input("Memory Usage: "))

if cpu < 80 and memory < 80:
    print("Cloud Instance Healthy")