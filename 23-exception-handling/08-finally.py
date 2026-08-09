try:
    file = open("server.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")