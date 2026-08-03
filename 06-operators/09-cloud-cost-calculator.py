aws_cost = float(input("Enter AWS Monthly Cost: "))
support_cost = float(input("Enter AWS Support Cost: "))

total_cost = aws_cost + support_cost

print("\n------ AWS Cost Report ------")

print("AWS Cost          :", aws_cost)
print("Support Cost      :", support_cost)
print("Total Monthly Cost:", total_cost)