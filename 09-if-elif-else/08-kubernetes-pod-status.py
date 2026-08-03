status = input("Enter Pod Status: ")

if status == "Running":
    print("Pod is Healthy")
elif status == "Pending":
    print("Pod is Starting")
elif status == "CrashLoopBackOff":
    print("Pod is Failing")
else:
    print("Unknown Status")