image = "nginx:latest"

if image.endswith(":latest"):
    print("Warning: Using latest tag")

if image.startswith("nginx"):
    print("Nginx image detected")