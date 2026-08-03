memory = int(input("Enter Memory Usage (%): "))

if memory > 90:
    print("Critical Alert")
elif memory >= 70:
    print("Warning Alert")
else:
    print("Memory Usage Normal")