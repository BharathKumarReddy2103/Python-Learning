def calculate_salary(salary, bonus):

    total = salary + bonus

    return total

salary = float(input("Salary: "))

bonus = float(input("Bonus: "))

total = calculate_salary(salary, bonus)

print("Total Salary:", total)