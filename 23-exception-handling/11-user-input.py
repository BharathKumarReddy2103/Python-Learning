try:
    environment = input("Enter Environment: ")

    if environment == "":
        raise ValueError("Environment cannot be empty")

    print("Environment:", environment)

except ValueError as error:
    print("Input Error:", error)