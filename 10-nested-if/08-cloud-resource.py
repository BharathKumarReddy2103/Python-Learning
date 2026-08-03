instance = input("EC2 Running? (yes/no): ")

if instance == "yes":

    cpu = int(input("CPU Usage (%): "))

    if cpu < 80:

        print("Instance Healthy")