environment = input("Enter Environment: ")

environment = environment.strip().lower()

if environment == "production":
    print("Production Environment")
elif environment == "staging":
    print("Staging Environment")
elif environment == "development":
    print("Development Environment")
else:
    print("Unknown Environment")