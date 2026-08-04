# Lists

## Objective

Learn how to store, organize, and manage multiple values using Python Lists.

Lists are one of the most frequently used data structures in Python. They allow us to store multiple related items in a single variable, making programs more efficient, readable, and scalable.

Lists are heavily used in automation, DevOps, cloud scripting, backend development, data processing, and API responses.

---

## Why Lists Exist

Imagine managing multiple servers without lists.

Instead of writing:

```python
server1 = "web01"
server2 = "web02"
server3 = "db01"
server4 = "redis01"
server5 = "app01"
```

You can simply write:

```python
servers = [
    "web01",
    "web02",
    "db01",
    "redis01",
    "app01"
]
```

Now you can process all servers using a loop instead of writing repetitive code.

Lists help us write cleaner, shorter, and more maintainable programs.

---

## Concepts Covered

- Creating Lists
- Accessing Elements
- Positive Indexing
- Negative Indexing
- Updating List Items
- Adding New Items
- Removing Items
- Iterating Through Lists
- List Length using `len()`
- Lists in Real-World DevOps Automation

---

## Files

### 01-basic-list.py

Create a simple Python list and print it.

---

### 02-index.py

Access list elements using positive indexes.

Example:

```python
servers[0]
servers[1]
servers[2]
```

---

### 03-negative-index.py

Access list elements from the end using negative indexes.

Example:

```python
servers[-1]
servers[-2]
```

---

### 04-update-list.py

Update an existing item inside a list.

Example:

```python
servers[1] = "app01"
```

---

### 05-add-item.py

Add a new item using `append()`.

Example:

```python
servers.append("db01")
```

---

### 06-remove-item.py

Remove an existing item using `remove()`.

Example:

```python
servers.remove("web02")
```

---

### 07-loop-list.py

Loop through every item in a list using a `for` loop.

---

### 08-aws-servers.py

Simulates checking multiple AWS EC2 instances stored in a list.

---

### 09-kubernetes-pods.py

Simulates monitoring Kubernetes Pods using a list.

---

### 10-devops-inventory.py

Demonstrates a DevOps inventory system that stores multiple servers in a list and processes them one by one.

---

## Repository Structure

```text
14-lists/

│── README.md
│── 01-basic-list.py
│── 02-index.py
│── 03-negative-index.py
│── 04-update-list.py
│── 05-add-item.py
│── 06-remove-item.py
│── 07-loop-list.py
│── 08-aws-servers.py
│── 09-kubernetes-pods.py
│── 10-devops-inventory.py
```

---

## How to Run

```bash
python 01-basic-list.py
python 02-index.py
python 03-negative-index.py
python 04-update-list.py
python 05-add-item.py
python 06-remove-item.py
python 07-loop-list.py
python 08-aws-servers.py
python 09-kubernetes-pods.py
python 10-devops-inventory.py
```

---

## Internal Working

When a list is created, Python allocates memory to store multiple objects.

Example:

```python
servers = [
    "web01",
    "web02",
    "db01"
]
```

Memory representation:

```
servers
   │
   ▼

+---------------------------+
| web01 | web02 | db01 |
+---------------------------+

Index
0       1       2
```

The variable `servers` stores a reference to the list object, not the actual values.

---

## Real-World DevOps Usage

Lists are used extensively in DevOps and Cloud automation.

Examples include:

### AWS

```python
ec2_instances = [
    "frontend",
    "backend",
    "database",
    "redis"
]
```

Used to iterate over EC2 instances for monitoring or automation.

---

### Kubernetes

```python
pods = [
    "frontend",
    "cart",
    "payment",
    "shipping"
]
```

Used to process Pods returned by the Kubernetes API.

---

### Ansible

Inventory files internally become collections that can be processed similarly to Python lists.

---

### Docker

Loop through running containers.

---

### GitHub

Process repositories returned by the GitHub API.

---

### CI/CD

Deploy applications to multiple servers stored in a list.

---

## Learning Outcome

After completing this lesson, you will be able to:

- Create Python Lists.
- Store multiple values in one variable.
- Access elements using indexes.
- Use positive and negative indexing.
- Update existing list items.
- Add new elements dynamically.
- Remove unwanted elements.
- Iterate through lists using loops.
- Count list elements using `len()`.
- Apply lists in DevOps, AWS, Kubernetes, Docker, GitHub, and automation projects.

---

## What's Next

Next lesson:

**15-list-methods**

You will learn powerful built-in list methods including:

- append()
- extend()
- insert()
- remove()
- pop()
- clear()
- sort()
- reverse()
- copy()
- count()
- index()

These methods are widely used in production-grade Python applications and automation scripts.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation