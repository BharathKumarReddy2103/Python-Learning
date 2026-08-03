server = input("Server Running? (yes/no): ")

if server == "yes":

    disk = int(input("Disk Usage (%): "))

    if disk < 80:

        print("Server Healthy")