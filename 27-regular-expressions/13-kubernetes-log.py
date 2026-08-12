import re

log = """
2026-08-12 19:35:10 INFO Pod frontend started
2026-08-12 19:35:15 ERROR Pod frontend CrashLoopBackOff
2026-08-12 19:35:20 INFO Pod backend Running
"""

pods = re.findall(r"Pod (\w+)", log)

print("Pods:", pods)

if re.search(r"ERROR", log):
    print("Kubernetes error detected")
else:
    print("Kubernetes logs healthy")