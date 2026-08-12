import json

data = '''
{
    "application": "roboshop",
    "environment": "production",
    "pipeline": "roboshop-deployment",
    "status": "success",
    "build": 125
}
'''

pipeline = json.loads(data)

print("Application :", pipeline["application"])
print("Environment :", pipeline["environment"])
print("Pipeline    :", pipeline["pipeline"])
print("Status      :", pipeline["status"])
print("Build       :", pipeline["build"])

if pipeline["status"] == "success":
    print("Deployment successful")
else:
    print("Deployment failed")