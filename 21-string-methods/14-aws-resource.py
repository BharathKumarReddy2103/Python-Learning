resources = "EC2,S3,RDS,EKS"

resource_list = resources.split(",")

for resource in resource_list:
    print("Checking AWS:", resource.strip())