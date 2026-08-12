import json

data = '''
{
    "instance_id": "i-123456",
    "region": "ap-south-1",
    "state": "running",
    "instance_type": "t3.medium"
}
'''

instance = json.loads(data)

print("AWS Instance:", instance["instance_id"])
print("Region:", instance["region"])
print("State:", instance["state"])
print("Instance Type:", instance["instance_type"])

if instance["state"] == "running":
    print("EC2 instance is running")
else:
    print("EC2 instance is not running")