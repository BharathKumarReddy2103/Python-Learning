deployment = {
    "application": "roboshop",
    "environment": "production",
    "status": "success"
}

try:
    application = deployment["application"]
    environment = deployment["environment"]
    status = deployment["status"]

    if status != "success":
        raise RuntimeError("Deployment failed")

    print("Application :", application)
    print("Environment :", environment)
    print("Status      :", status)

except KeyError as error:
    print("Deployment configuration missing:", error)

except RuntimeError as error:
    print("Deployment Error:", error)