try:
    number = int("100")
    print(number)
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful")