# Dictionary Methods

## Objective

Learn the most commonly used Python dictionary methods for accessing, updating, copying, deleting, and iterating over key-value pairs.

Dictionary methods are heavily used in backend development, DevOps automation, cloud SDKs, Infrastructure as Code (IaC), and REST API integrations because most configuration data is represented as dictionaries.

---

## Why Dictionary Methods Matter

Dictionaries are one of the most frequently used data structures in Python.

In real-world applications they are used to:

- Process JSON API responses
- Store application configurations
- Manage cloud resources
- Handle Kubernetes object metadata
- Work with AWS Boto3 responses
- Parse Terraform outputs
- Read YAML configuration files
- Build FastAPI request and response models

Learning dictionary methods is essential before working with REST APIs, FastAPI, automation scripts, and cloud SDKs.

---

## Concepts Covered

- get()
- update()
- pop()
- popitem()
- clear()
- copy()
- keys()
- values()
- items()

---

## Project Structure

```text
18-dictionary-methods/
│
├── 01-get.py
├── 02-update.py
├── 03-pop.py
├── 04-popitem.py
├── 05-clear.py
├── 06-copy.py
├── 07-keys.py
├── 08-values.py
├── 09-items.py
├── 10-devops-config.py
└── README.md
```

---

# Scripts Overview

## 01-get.py

Learn how to safely retrieve values using the `get()` method.

Concepts:

- Existing key
- Missing key
- Default value

---

## 02-update.py

Update existing dictionary values and add new key-value pairs.

Concepts:

- update()
- Merge dictionaries
- Modify configuration

---

## 03-pop.py

Remove a specific key from a dictionary.

Concepts:

- pop()
- Delete by key

---

## 04-popitem.py

Remove the last inserted key-value pair.

Concepts:

- popitem()

---

## 05-clear.py

Remove all entries from a dictionary.

Concepts:

- clear()

---

## 06-copy.py

Create a copy of an existing dictionary.

Concepts:

- copy()
- Independent dictionary object

---

## 07-keys.py

Retrieve all dictionary keys.

Concepts:

- keys()
- Iteration

---

## 08-values.py

Retrieve all dictionary values.

Concepts:

- values()

---

## 09-items.py

Loop through key-value pairs.

Concepts:

- items()
- Tuple unpacking

---

## 10-devops-config.py

Real-world DevOps configuration management.

Concepts:

- Configuration dictionaries
- update()
- get()
- items()
- Infrastructure configuration

---

# Real-World DevOps Examples

## AWS SDK (Boto3)

```python
instance = {
    "InstanceId": "i-123456",
    "State": "running",
    "Region": "ap-south-1"
}

print(instance.get("State"))
```

---

## Kubernetes Object

```python
pod = {
    "name": "frontend",
    "namespace": "default",
    "status": "Running"
}
```

---

## Terraform Output

```python
terraform = {
    "vpc": "vpc-12345",
    "subnet": "subnet-67890"
}
```

---

## GitHub Actions Variables

```python
env = {
    "BRANCH": "main",
    "BUILD": "102"
}
```

---

## FastAPI JSON Response

```python
response = {
    "status": "success",
    "message": "User Created"
}
```

---

# Learning Outcome

After completing this lesson, you will be able to:

- Access dictionary values safely
- Update and merge dictionaries
- Remove dictionary entries
- Copy dictionaries
- Iterate over keys and values
- Process configuration data
- Handle JSON responses
- Work with cloud SDK outputs
- Build backend applications using dictionaries
- Understand how FastAPI and REST APIs exchange data internally

---

# Prerequisites

Complete the previous lessons before continuing:

- Variables
- Data Types
- Operators
- Conditional Statements
- Loops
- Functions
- Lists
- List Methods
- Tuples
- Dictionaries

---

# Next Lesson

**19 - Sets**

Topics include:

- Creating Sets
- Unique Values
- add()
- update()
- remove()
- discard()
- pop()
- union()
- intersection()
- difference()

These concepts are useful for removing duplicate values, comparing datasets, managing AWS regions, Kubernetes namespaces, IAM users, security groups, and cloud inventory.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation