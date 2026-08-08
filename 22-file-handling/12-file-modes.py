file = open("file-modes.txt", "w")
file.write("Initial configuration\n")
file.close()

file = open("file-modes.txt", "a")
file.write("Additional configuration\n")
file.close()

file = open("file-modes.txt", "r")
data = file.read()
file.close()

print(data)