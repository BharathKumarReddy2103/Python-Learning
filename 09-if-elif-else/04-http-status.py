status = int(input("Enter HTTP Status Code: "))

if status == 200:
    print("Success")
elif status == 404:
    print("Page Not Found")
elif status == 500:
    print("Internal Server Error")
else:
    print("Unknown Status Code")