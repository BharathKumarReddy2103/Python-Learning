ec2_instances = [
    "frontend",
    "backend",
    "database",
    "redis"
]

for instance in ec2_instances:
    print("Checking EC2:", instance)