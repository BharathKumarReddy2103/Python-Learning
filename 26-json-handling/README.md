# JSON Handling

## Objective

Learn the fundamentals of working with JSON in Python, including parsing JSON data, converting Python objects to JSON, handling JSON files, working with nested JSON, processing API responses, and using JSON for real-world DevOps automation.

JSON is one of the most commonly used data formats in modern software development, cloud automation, APIs, CI/CD pipelines, Kubernetes, and DevOps tooling.

---

## Why JSON Handling Matters

DevOps engineers work with structured data every day.

Examples include:

- AWS CLI JSON output
- Kubernetes API responses
- REST API responses
- CI/CD pipeline data
- Server inventories
- Monitoring metrics
- Application configuration
- Infrastructure configuration
- Deployment information
- Cloud resource information

Python provides the built-in `json` module to easily convert between JSON and Python data structures.

---

## Concepts Covered

- JSON basics
- Python `json` module
- `json.loads()`
- `json.dumps()`
- JSON objects
- JSON arrays
- JSON strings
- JSON numbers
- JSON booleans
- JSON `null`
- Python dictionaries and JSON
- Python lists and JSON
- Nested JSON
- `json.load()`
- `json.dump()`
- Reading JSON files
- Writing JSON files
- Processing AWS-style JSON
- Processing Kubernetes-style JSON
- Processing API responses
- Processing CI/CD JSON
- Processing DevOps configuration
- Processing server inventory
- Processing monitoring data

---

## JSON and Python Data Types

JSON data maps naturally to Python data types.

| JSON | Python |
|---|---|
| Object | `dict` |
| Array | `list` |
| String | `str` |
| Number | `int` / `float` |
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

Example:

JSON:

```text
{
    "name": "web01",
    "port": 8080,
    "healthy": true,
    "backup": null
}
```

Python representation:

```text
{
    "name": "web01",
    "port": 8080,
    "healthy": True,
    "backup": None
}
```

---

## JSON String to Python Object

Use `json.loads()` when JSON data is available as a string.

```python
import json

data = '{"name": "web01", "status": "Running"}'

server = json.loads(data)

print(server)
print(type(server))
```

Output:

```text
{'name': 'web01', 'status': 'Running'}
<class 'dict'>
```

---

## Python Object to JSON String

Use `json.dumps()` when converting a Python object into JSON.

```python
import json

server = {
    "name": "web01",
    "status": "Running"
}

data = json.dumps(server)

print(data)
print(type(data))
```

Output:

```text
{"name": "web01", "status": "Running"}
<class 'str'>
```

---

## JSON File to Python Object

Use `json.load()` to read JSON directly from a file.

```python
import json

with open("server.json", "r") as file:
    server = json.load(file)

print(server)
```

---

## Python Object to JSON File

Use `json.dump()` to write Python data into a JSON file.

```python
import json

server = {
    "name": "web01",
    "status": "Running"
}

with open("server-output.json", "w") as file:
    json.dump(server, file, indent=4)
```

---

## Project Structure

```text
26-json-handling/
│
├── 01-basic-json.py
├── 02-json-loads.py
├── 03-json-dumps.py
├── 04-json-types.py
├── 05-json-list.py
├── 06-json-nested.py
├── 07-json-load-file.py
├── 08-json-write-file.py
├── 09-aws-json.py
├── 10-kubernetes-json.py
├── 11-api-json.py
├── 12-cicd-json.py
├── 13-devops-config-json.py
├── 14-json-server-inventory.py
├── 15-json-monitoring.py
├── server.json
├── server-output.json
└── README.md
```

---

## Script 01 - Basic JSON

### `01-basic-json.py`

Introduction to JSON data and the Python `json` module.

Example:

```python
import json

server = {
    "name": "web01",
    "status": "Running"
}

print(json.dumps(server))
```

Output:

```text
{"name": "web01", "status": "Running"}
```

---

## Script 02 - json.loads()

### `02-json-loads.py`

Converts a JSON string into a Python dictionary.

```python
import json

data = '{"name": "web01", "status": "Running"}'

server = json.loads(data)

print(server)
print(type(server))
```

Output:

```text
{'name': 'web01', 'status': 'Running'}
<class 'dict'>
```

---

## Script 03 - json.dumps()

### `03-json-dumps.py`

Converts a Python dictionary into a JSON string.

```python
import json

server = {
    "name": "web01",
    "status": "Running"
}

data = json.dumps(server)

print(data)
print(type(data))
```

Output:

```text
{"name": "web01", "status": "Running"}
<class 'str'>
```

---

## Script 04 - JSON Types

### `04-json-types.py`

Learn how different JSON data types are represented in Python.

Example data:

```text
{
    "name": "web01",
    "port": 8080,
    "healthy": true,
    "backup": null
}
```

Output:

```text
Name: web01
Port: 8080
Healthy: True
Backup: None
<class 'str'>
<class 'int'>
<class 'bool'>
<class 'NoneType'>
```

---

## Script 05 - JSON List

### `05-json-list.py`

Learn how JSON arrays are represented as Python lists.

Example:

```text
["web01", "web02", "db01"]
```

Output:

```text
['web01', 'web02', 'db01']
Server: web01
Server: web02
Server: db01
```

---

## Script 06 - Nested JSON

### `06-json-nested.py`

Learn how to access values inside nested JSON structures.

Example:

```text
{
    "server": {
        "name": "web01",
        "ip": "10.0.0.10",
        "port": 8080
    }
}
```

Output:

```text
Server: web01
IP: 10.0.0.10
Port: 8080
```

---

## Script 07 - Load JSON File

### `07-json-load-file.py`

Read structured server information from a JSON file.

Example output:

```text
Name: web01
Environment: production
Status: Running
```

---

## Script 08 - Write JSON File

### `08-json-write-file.py`

Create a JSON file from Python data.

Output:

```text
JSON file created
```

This script demonstrates how Python automation can generate structured JSON configuration or output files.

---

## Script 09 - AWS JSON

### `09-aws-json.py`

Process AWS-style JSON data.

Example output:

```text
AWS Instance: i-123456
Region: ap-south-1
State: running
Instance Type: t3.medium
EC2 instance is running
```

This represents the type of structured data commonly returned by AWS CLI commands and APIs.

---

## Script 10 - Kubernetes JSON

### `10-kubernetes-json.py`

Process Kubernetes-style resource information.

Example output:

```text
Pod: frontend
Namespace: production
Status: Running
Pod is healthy
```

Kubernetes provides structured resource information that can be processed using Python.

---

## Script 11 - API JSON

### `11-api-json.py`

Process JSON returned from an API.

Example output:

```text
Status Code: 200
API request successful
Current User URL: https://api.github.com/user
Repository URL: https://api.github.com/repos/{owner}/{repo}
```

This demonstrates the relationship between HTTP APIs and JSON data.

---

## Script 12 - CI/CD JSON

### `12-cicd-json.py`

Process CI/CD pipeline information stored as JSON.

Example output:

```text
Application : roboshop
Environment : production
Pipeline    : roboshop-deployment
Status      : success
Build       : 125
Deployment successful
```

This is useful for automation scripts that need to inspect pipeline status and deployment results.

---

## Script 13 - DevOps Configuration JSON

### `13-devops-config-json.py`

Process structured DevOps configuration.

Example output:

```text
Environment : production
Region      : ap-south-1
Platform    : EKS
Namespace   : roboshop
Replicas    : 3
```

This type of structure can represent deployment or environment configuration.

---

## Script 14 - JSON Server Inventory

### `14-json-server-inventory.py`

Process server inventory information stored as JSON.

Example output:

```text
Server: web01 | IP: 10.0.0.10 | Role: frontend | Status: running
Server: web02 | IP: 10.0.0.11 | Role: frontend | Status: running
Server: db01 | IP: 10.0.0.20 | Role: database | Status: running
```

This demonstrates how JSON can be used to represent infrastructure inventory.

---

## Script 15 - JSON Monitoring

### `15-json-monitoring.py`

Process monitoring metrics stored as JSON.

Example output:

```text
Server: web01
CPU Usage: 45 %
Memory Usage: 82 %
Disk Usage: 60 %
CPU usage normal
High memory usage
Disk usage normal
```

This demonstrates how Python can process monitoring information and perform basic health checks.

---

## Real-World DevOps Applications

JSON handling is heavily used in DevOps automation.

### AWS

Process AWS CLI and API responses:

```text
AWS CLI
   ↓
JSON
   ↓
Python
   ↓
Analyze resources
```

Examples:

* EC2 instances
* S3 buckets
* RDS databases
* EKS clusters
* IAM resources
* VPC information

---

### Kubernetes

Process Kubernetes API and CLI output:

```text
Kubernetes
     ↓
JSON
     ↓
Python
     ↓
Analyze resources
```

Examples:

* Pods
* Deployments
* Services
* Nodes
* Namespaces
* ConfigMaps
* Secrets

---

### CI/CD

Process pipeline information:

```text
CI/CD Pipeline
      ↓
JSON
      ↓
Python
      ↓
Check Status
      ↓
Deployment Decision
```

Examples:

* Build status
* Test status
* Deployment status
* Build number
* Application name
* Environment

---

### Monitoring

Process monitoring metrics:

```text
Monitoring System
       ↓
      JSON
       ↓
     Python
       ↓
Health Check
       ↓
Alert / Report
```

Examples:

* CPU usage
* Memory usage
* Disk usage
* Application status
* Server health

---

## Important JSON Functions

### `json.loads()`

Converts JSON string to Python object.

```python
json.loads(data)
```

---

### `json.dumps()`

Converts Python object to JSON string.

```python
json.dumps(data)
```

---

### `json.load()`

Reads JSON from a file.

```python
json.load(file)
```

---

### `json.dump()`

Writes JSON to a file.

```python
json.dump(data, file)
```

---

## JSON Conversion Flow

The four most important operations can be remembered like this:

```text
JSON String
    |
    | json.loads()
    ↓
Python Object
    |
    | json.dumps()
    ↓
JSON String
```

For files:

```text
JSON File
    |
    | json.load()
    ↓
Python Object
    |
    | json.dump()
    ↓
JSON File
```

---

## JSON vs Python Dictionary

A Python dictionary:

```python
server = {
    "name": "web01",
    "status": "Running"
}
```

A JSON string:

```text
{"name": "web01", "status": "Running"}
```

They may look similar, but they are different types.

```python
print(type(server))
```

Output:

```text
<class 'dict'>
```

After:

```python
data = json.dumps(server)
```

The result is:

```text
<class 'str'>
```

Understanding this difference is very important when working with APIs and configuration files.

---

## Learning Outcome

After completing this lesson, you will be able to:

* Understand the JSON format
* Use Python's built-in `json` module
* Convert JSON strings into Python objects
* Convert Python objects into JSON strings
* Read JSON files
* Write JSON files
* Work with JSON dictionaries
* Work with JSON lists
* Access nested JSON data
* Process AWS-style JSON
* Process Kubernetes-style JSON
* Process API responses
* Process CI/CD pipeline data
* Process DevOps configuration
* Process server inventory data
* Process monitoring metrics
* Use JSON in DevOps automation scripts

---

## Key Takeaways

Remember these four functions:

```text
json.loads()  → JSON string → Python object

json.dumps()  → Python object → JSON string

json.load()   → JSON file → Python object

json.dump()   → Python object → JSON file
```

These four operations form the foundation of JSON processing in Python.

---

## Next Lesson

**27 - Regular Expressions**

Topics include:

* Regular expressions
* Pattern matching
* `re.search()`
* `re.match()`
* `re.findall()`
* `re.sub()`
* Character classes
* Quantifiers
* Groups
* Log parsing
* IP address extraction
* Kubernetes log analysis
* Configuration validation
* DevOps automation

Regular expressions are especially useful for extracting and validating information from logs, command output, configuration files, and other text-based data.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation