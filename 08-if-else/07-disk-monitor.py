disk_usage = int(input("Enter Disk Usage (%): "))

if disk_usage > 80:
    print("Warning: Disk usage is high")
else:
    print("Disk usage is normal")