import re

log = """
INFO: Deployment started
INFO: Docker image pulled
WARNING: High memory usage
ERROR: Kubernetes pod failed
INFO: Deployment completed
ERROR: Database connection failed
"""

info_count = len(re.findall(r"INFO:", log))
warning_count = len(re.findall(r"WARNING:", log))
error_count = len(re.findall(r"ERROR:", log))

print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)

if error_count > 0:
    print("Critical errors detected")
else:
    print("No critical errors detected")