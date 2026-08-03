cost = float(input("Enter Monthly AWS Cost: "))

if cost >= 100000:
    print("High Cloud Spending")
elif cost >= 50000:
    print("Medium Cloud Spending")
else:
    print("Low Cloud Spending")