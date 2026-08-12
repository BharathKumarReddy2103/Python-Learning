import json

data = '''
{
    "metadata": {
        "name": "frontend",
        "namespace": "production"
    },
    "status": {
        "phase": "Running"
    }
}
'''

pod = json.loads(data)

name = pod["metadata"]["name"]
namespace = pod["metadata"]["namespace"]
status = pod["status"]["phase"]

print("Pod:", name)
print("Namespace:", namespace)
print("Status:", status)

if status == "Running":
    print("Pod is healthy")
else:
    print("Pod is not healthy")