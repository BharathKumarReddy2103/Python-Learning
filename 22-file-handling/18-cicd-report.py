deployment = [
    "CI/CD Deployment Report\n",
    "-----------------------\n",
    "Application: Roboshop\n",
    "Environment: Production\n",
    "Platform: Kubernetes\n",
    "Status: Successful\n",
    "Image: roboshop/frontend:1.0\n"
]

with open("deployment-report.txt", "w") as file:
    file.writelines(deployment)

print("Deployment report generated")