config = {
    "environment": "production",
    "region": "ap-south-1",
    "platform": "EKS",
    "iac": "Terraform",
    "cicd": "GitHub Actions"
}

print("Environment :", config.get("environment"))
print("Region      :", config.get("region"))
print("Platform    :", config.get("platform"))

config.update({
    "monitoring": "Prometheus"
})

print()

for key, value in config.items():
    print(key, ":", value)