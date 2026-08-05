# List Methods

## Objective

Learn how to use Python list methods to add, update, remove, search, copy, and organize data.

List methods make it easy to manipulate collections of data efficiently. They are heavily used in automation scripts, backend development, DevOps tooling, cloud automation, and data processing.

---

# Why List Methods Exist

Creating a list is only the beginning.

Real applications constantly modify data.

For example:

- Adding a new EC2 instance
- Removing a failed Kubernetes pod
- Sorting server names
- Searching for a user
- Counting unhealthy nodes
- Copying configurations

Python provides built-in methods that make these operations simple and efficient.

---

# Concepts Covered

- append()
- extend()
- insert()
- remove()
- pop()
- clear()
- sort()
- reverse()
- count()
- index()
- copy()

---

# Files

## 01-append.py

Adds a single item to the end of a list using `append()`.

---

## 02-extend.py

Adds multiple items from another list using `extend()`.

---

## 03-insert.py

Inserts an item at a specific position using `insert()`.

---

## 04-remove.py

Removes an item by value using `remove()`.

---

## 05-pop.py

Removes and returns the last item (or a specified index) using `pop()`.

---

## 06-clear.py

Removes all items from a list using `clear()`.

---

## 07-sort.py

Sorts list elements in ascending order.

---

## 08-reverse.py

Reverses the order of elements in a list.

---

## 09-count.py

Counts how many times an item appears in a list.

---

## 10-index.py

Finds the position of an item inside a list.

---

## 11-copy.py

Creates a copy of an existing list.

---

## 12-aws-servers.py

Uses list methods to manage AWS EC2 server names.

Real-world example:
- Add new servers
- Remove terminated instances
- Display current infrastructure

---

## 13-kubernetes-pods.py

Uses list methods to manage Kubernetes pods.

Example operations:

- Remove completed pods
- Add newly created pods
- Display running workloads

---

## 14-devops-inventory.py

Maintains a DevOps inventory list.

Example:

- Add servers
- Sort inventory
- Display all servers

---

## 15-cloud-resource-manager.py

A practical cloud resource management example using multiple list methods together.

Operations include:

- Add cloud resources
- Sort resources
- Iterate through the inventory
- Display available services

---

# Commands

```bash
python 01-append.py
python 02-extend.py
python 03-insert.py
python 04-remove.py
python 05-pop.py
python 06-clear.py
python 07-sort.py
python 08-reverse.py
python 09-count.py
python 10-index.py
python 11-copy.py
python 12-aws-servers.py
python 13-kubernetes-pods.py
python 14-devops-inventory.py
python 15-cloud-resource-manager.py
```

---

# Learning Outcome

After completing this lesson, you will be able to:

- Add items to a list.
- Add multiple items at once.
- Insert elements at specific positions.
- Remove elements safely.
- Retrieve and remove elements using `pop()`.
- Empty an entire list.
- Sort collections.
- Reverse collections.
- Search for values.
- Count duplicate items.
- Copy lists correctly.
- Build inventory management scripts.

---

# Real-World DevOps Usage

List methods are widely used in:

- AWS EC2 inventory automation
- Kubernetes pod management
- Docker container tracking
- Ansible inventory generation
- Terraform resource processing
- CI/CD pipeline execution
- Monitoring unhealthy servers
- Log collection
- Configuration management
- Infrastructure reporting

---

# Internal Execution

When Python executes a list method like:

```python
servers.append("web03")
```

Python performs the following steps:

1. Finds the memory location of the list object.
2. Checks whether there is enough allocated space.
3. If needed, resizes the list internally.
4. Stores the new object's reference.
5. Updates the list length.

The original list object is modified in memory.

Example:

Before:

```
servers
│
├── web01
├── web02
└── db01
```

After:

```
servers
│
├── web01
├── web02
├── db01
└── web03
```

Unlike strings, lists are **mutable**, meaning their contents can change without creating a new object.

---

# Summary

In this lesson you learned how to manipulate lists using Python's built-in methods.

These methods form the foundation of real-world automation because most production programs work with collections of data such as servers, users, pods, cloud resources, API responses, and configuration files.