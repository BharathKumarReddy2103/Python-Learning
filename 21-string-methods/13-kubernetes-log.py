log = "  ERROR: Pod frontend is CrashLoopBackOff  "

log = log.strip()

print("Log:", log)

if log.lower().startswith("error"):
    print("Critical Kubernetes Error")

if "CrashLoopBackOff" in log:
    print("Pod is failing")