def check_pod(status):

    if status == "Running":
        print("Pod Healthy")

    else:
        print("Pod Failed")

status = input("Pod Status: ")

check_pod(status)