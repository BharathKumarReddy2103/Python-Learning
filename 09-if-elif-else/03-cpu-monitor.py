cpu = int(input("Enter CPU Usage (%): "))

if cpu > 80:
    print("Critical")
elif cpu >= 50:
    print("Warning")
else:
    print("Healthy")