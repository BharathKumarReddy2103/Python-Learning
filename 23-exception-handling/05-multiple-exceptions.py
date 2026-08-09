try:
    number = int("python")
    result = 10 / number
    print(result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")