environment = "production"

try:
    if environment not in ["development", "staging", "production"]:
        raise ValueError("Invalid environment")

    print("Environment:", environment)

except ValueError as error:
    print("Configuration Error:", error)