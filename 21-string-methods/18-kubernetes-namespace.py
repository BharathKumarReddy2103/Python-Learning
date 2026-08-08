namespace = "  production  "

namespace = namespace.strip().lower()

if namespace.startswith("prod"):
    print("Production namespace detected")
else:
    print("Non-production namespace")