import json

data = '''
{
    "environment": "production",
    "region": "ap-south-1",
    "platform": "EKS",
    "namespace": "roboshop",
    "replicas": 3
}
'''

config = json.loads(data)

print("Environment :", config["environment"])
print("Region      :", config["region"])
print("Platform    :", config["platform"])
print("Namespace   :", config["namespace"])
print("Replicas    :", config["replicas"])