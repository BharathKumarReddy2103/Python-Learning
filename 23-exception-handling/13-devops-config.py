config = {
    "environment": "production",
    "region": "ap-south-1",
    "platform": "EKS"
}

try:
    environment = config["environment"]
    region = config["region"]
    platform = config["platform"]

    print("Environment :", environment)
    print("Region      :", region)
    print("Platform    :", platform)

except KeyError as error:
    print("Missing configuration:", error)