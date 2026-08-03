salary = float(input("Enter your monthly salary: "))
bonus_percentage = float(input("Enter bonus percentage: "))

bonus_amount = salary * bonus_percentage / 100

total_salary = salary + bonus_amount

print("\n------ Salary Details ------")

print("Monthly Salary    :", salary)
print("Bonus Percentage  :", bonus_percentage, "%")
print("Bonus Amount      :", bonus_amount)
print("Total Salary      :", total_salary)