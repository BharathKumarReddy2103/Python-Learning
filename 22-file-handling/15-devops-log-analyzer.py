with open("devops.log", "r") as file:
    logs = file.read()

if "ERROR" in logs:
    print("Deployment contains errors")
elif "WARNING" in logs:
    print("Deployment contains warnings")
else:
    print("Deployment completed successfully")