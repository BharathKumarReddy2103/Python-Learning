# Dictionaries

## Objective

Learn how to use Python dictionaries to store, access, update, and manage data using **key-value pairs**.

Dictionaries are one of the most powerful and widely used data structures in Python. They are heavily used in DevOps automation, cloud SDKs, REST APIs, JSON processing, configuration management, and infrastructure scripting.

---

## Theory

A dictionary stores data as **key-value pairs**.

Unlike lists, which access data using numeric indexes, dictionaries access data using meaningful keys.

Example:

```python
server = {
    "name": "web01",
    "ip": "10.0.0.10",
    "status": "Running"
}
```

Accessing values:

```python
print(server["name"])
```

Output:

```
web01
```

---

## Why Dictionaries Exist

Imagine AWS returns the following information:

```text
InstanceId : i-123456
Region     : ap-south-1
State      : Running
```

Using a list:

```python
[
    "i-123456",
    "ap-south-1",
    "Running"
]
```

Which index represents the region?

Instead, dictionaries provide readable access:

```python
instance["Region"]
```

This makes code easier to read, maintain, and debug.

---

## Internal Execution

When Python creates a dictionary:

```python
server = {
    "name": "web01",
    "ip": "10.0.0.10"
}
```

Python stores it internally as a hash table.

```
server
   │
   ▼
Dictionary
 ├── name ─────► web01
 └── ip ───────► 10.0.0.10
```

Searching by key is extremely fast.

```
server["ip"]
```

Average lookup time is **O(1)**.

This is why dictionaries are heavily used throughout Python.

---

## Concepts Covered

- Creating dictionaries
- Accessing values
- Updating values
- Adding new keys
- Removing keys
- Iterating through dictionaries
- Using `keys()`
- Using `values()`
- Real-world DevOps examples

---

## Files

### 01-basic-dictionary.py

Creates a simple dictionary.

### 02-access-value.py

Accesses dictionary values using keys.

### 03-update-value.py

Updates an existing value.

### 04-add-key.py

Adds a new key-value pair.

### 05-remove-key.py

Removes a key using `del`.

### 06-loop-dictionary.py

Loops through dictionary keys and prints values.

### 07-keys-values.py

Displays all keys and values using dictionary methods.

### 08-aws-ec2.py

Represents AWS EC2 instance information using a dictionary.

### 09-kubernetes-pod.py

Stores Kubernetes Pod metadata in a dictionary.

### 10-devops-server.py

Represents a production server configuration using key-value pairs.

---

## Commands

```bash
python 01-basic-dictionary.py
python 02-access-value.py
python 03-update-value.py
python 04-add-key.py
python 05-remove-key.py
python 06-loop-dictionary.py
python 07-keys-values.py
python 08-aws-ec2.py
python 09-kubernetes-pod.py
python 10-devops-server.py
```

---

## Learning Outcome

After completing this lesson, you will be able to:

- Create dictionaries
- Access values using keys
- Update dictionary values
- Add new key-value pairs
- Remove dictionary entries
- Iterate through dictionaries
- Understand how Python stores structured data
- Work with AWS, Kubernetes, and API responses represented as dictionaries

---

## Real-World DevOps Usage

Dictionaries are everywhere in DevOps and cloud automation.

Examples include:

- AWS Boto3 SDK responses
- Azure SDK responses
- Google Cloud SDK responses
- Terraform variables
- Ansible host variables
- Kubernetes API objects
- Docker container inspection output
- GitHub Actions event payloads
- JSON configuration files
- REST API responses
- YAML configuration converted into Python objects

Whenever Python reads JSON data, it is usually converted into dictionaries and lists.

Understanding dictionaries is essential before learning JSON processing, REST APIs, FastAPI, and cloud automation.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation