resources = [
    "EC2",
    "RDS",
    "S3"
]

resources.append("EKS")

resources.sort()

for resource in resources:
    print(resource)