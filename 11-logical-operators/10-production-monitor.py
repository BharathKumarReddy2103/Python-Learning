cpu = int(input("CPU Usage: "))
disk = int(input("Disk Usage: "))

if cpu < 80 or disk < 80:
    print("System Running")
else:
    print("System Requires Attention")