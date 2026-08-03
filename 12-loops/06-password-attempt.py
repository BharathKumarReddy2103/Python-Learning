attempt = 1

while attempt <= 3:
    password = input("Enter Password: ")

    if password == "DevOps123":
        print("Login Successful")
        break

    print("Wrong Password")
    attempt += 1