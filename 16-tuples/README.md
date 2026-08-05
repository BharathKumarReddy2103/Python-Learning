# Tuples

## Objective

Learn how to use tuples in Python to store ordered, immutable collections of data.

A tuple is one of Python's built-in data structures. It is similar to a list, but unlike lists, tuples cannot be modified after creation. Tuples are commonly used for storing fixed configuration values, constants, and read-only collections.

---

## Concepts Covered

- Creating tuples
- Tuple syntax using `()`
- Accessing elements using indexes
- Negative indexing
- Iterating through tuples
- Finding tuple length using `len()`
- Membership testing using `in`
- Converting a list to a tuple
- Immutable collections
- Real-world DevOps configurations

---

## Files

### 01-basic-tuple.py

Creates and prints a simple tuple.

### 02-index.py

Accesses tuple elements using positive indexes.

### 03-negative-index.py

Accesses tuple elements using negative indexes.

### 04-loop.py

Loops through every element in a tuple.

### 05-length.py

Uses the `len()` function to determine the number of elements.

### 06-membership.py

Checks whether an element exists in a tuple using the `in` operator.

### 07-convert-list.py

Converts a list into a tuple using the `tuple()` function.

### 08-aws-regions.py

Stores supported AWS Regions in a tuple and prints each region.

### 09-kubernetes-namespaces.py

Stores Kubernetes namespaces as an immutable collection.

### 10-devops-config.py

Represents a fixed DevOps configuration using a tuple.

---

## Commands

Run any script using:

```bash
python 01-basic-tuple.py
python 02-index.py
python 03-negative-index.py
python 04-loop.py
python 05-length.py
python 06-membership.py
python 07-convert-list.py
python 08-aws-regions.py
python 09-kubernetes-namespaces.py
python 10-devops-config.py
```

Or simply click the **▶ Run** button in VS Code.

---

## Learning Outcome

After completing this lesson, you will be able to:

- Create tuples
- Access tuple elements using indexes
- Use positive and negative indexing
- Iterate through tuples using loops
- Check whether values exist using the `in` operator
- Convert lists into tuples
- Understand tuple immutability
- Know when to use tuples instead of lists

---

## Internal Working

When Python creates a tuple:

- Memory is allocated for the tuple object.
- References to all elements are stored.
- The tuple becomes immutable.
- The size and structure cannot be changed.

Because tuples are immutable, Python can optimize memory usage and access speed.

---

## Real-World DevOps Usage

Tuples are commonly used to store fixed values such as:

- AWS Regions
- Availability Zones
- Kubernetes Namespaces
- API Endpoints
- Deployment Environments
- CI/CD Stage Names
- Port Numbers
- Monitoring Alert Levels

Example:

```python
aws_regions = (
    "ap-south-1",
    "us-east-1",
    "eu-west-1"
)
```

Since AWS Regions are predefined, storing them in a tuple prevents accidental modification.

---

## Best Practices

- Use tuples for fixed configuration values.
- Use lists when data needs to change.
- Prefer tuples for read-only collections.
- Use meaningful variable names.
- Keep related values together.

---

## Interview Questions

1. What is a tuple?
2. What is the difference between a list and a tuple?
3. Why are tuples immutable?
4. When should you use tuples instead of lists?
5. Can tuples contain duplicate values?
6. Can tuples contain different data types?
7. How do you iterate through a tuple?
8. How do you convert a list into a tuple?
9. How do you check if an item exists in a tuple?
10. Why are tuples faster than lists?

---

## Common Mistakes

Trying to modify a tuple:

```python
servers = ("web01", "web02")

servers[0] = "app01"
```

Output:

```text
TypeError: 'tuple' object does not support item assignment
```

Trying to append to a tuple:

```python
servers.append("db01")
```

Output:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

---

## Summary

Tuples are ordered, immutable collections that provide better performance and safety when storing fixed data. They are widely used in Python applications for configuration values, cloud infrastructure settings, and read-only datasets.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation