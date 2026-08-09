try:
    with open("missing.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found")