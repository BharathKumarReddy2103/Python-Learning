import json

data = '''
{
    "server": "web01",
    "cpu_usage": 45,
    "memory_usage": 82,
    "disk_usage": 60
}
'''

metrics = json.loads(data)

print("Server:", metrics["server"])
print("CPU Usage:", metrics["cpu_usage"], "%")
print("Memory Usage:", metrics["memory_usage"], "%")
print("Disk Usage:", metrics["disk_usage"], "%")

if metrics["cpu_usage"] > 80:
    print("High CPU usage")
else:
    print("CPU usage normal")

if metrics["memory_usage"] > 80:
    print("High memory usage")
else:
    print("Memory usage normal")

if metrics["disk_usage"] > 80:
    print("High disk usage")
else:
    print("Disk usage normal")