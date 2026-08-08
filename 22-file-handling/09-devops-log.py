file = open("devops.log", "w")

file.write("INFO: Deployment started\n")
file.write("INFO: Docker image pulled\n")
file.write("INFO: Kubernetes deployment started\n")
file.write("INFO: Deployment completed successfully\n")

file.close()

print("DevOps Log Created")