# Functions

## Objective

Learn how to create reusable blocks of code using Python functions.

Functions help reduce duplicate code, improve readability, simplify maintenance, and make programs modular. They are one of the most fundamental concepts in software development and are used extensively in DevOps automation, backend development, cloud engineering, and system administration.

---

## What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, you define it once and call it whenever needed.

### Syntax

```python
def function_name():
    statements
```

Example:

```python
def greet():
    print("Hello DevOps Engineer")

greet()
```

Output

```text
Hello DevOps Engineer
```

---

## Why Functions?

Functions provide several advantages:

- Code Reusability
- Better Code Organization
- Easier Maintenance
- Improved Readability
- Modular Programming
- Reduced Code Duplication

---

## Function Execution Flow

```text
Program Starts
        │
        ▼
Python Reads Function Definition
        │
        ▼
Function Stored in Memory
        │
        ▼
Function Called
        │
        ▼
Execute Function Body
        │
        ▼
Return to Caller
        │
        ▼
Program Continues
```

---

## Concepts Covered

- Function Definition (`def`)
- Function Calling
- Multiple Function Calls
- Parameters
- Arguments
- Return Values
- Code Reusability
- Modular Programming
- Functions with Loops
- Real-world DevOps Examples

---

## Files

### 01-basic-function.py

Create and execute your first Python function.

---

### 02-call-function.py

Learn how a single function can be called multiple times.

---

### 03-multiple-functions.py

Create multiple functions and execute them independently.

---

### 04-function-with-parameter.py

Pass values into functions using parameters.

---

### 05-function-return.py

Learn how functions return values using the `return` keyword.

---

### 06-addition-function.py

Build a reusable addition function using parameters and return values.

---

### 07-salary-calculator.py

Real-world example that calculates employee salary using a reusable function.

---

### 08-cloud-cost.py

Calculate AWS monthly cloud cost using reusable functions.

---

### 09-kubernetes-health.py

Validate Kubernetes Pod health using a function.

---

### 10-devops-monitor.py

Combine functions with loops to monitor multiple servers.

---

## Commands

```bash
python 01-basic-function.py
python 02-call-function.py
python 03-multiple-functions.py
python 04-function-with-parameter.py
python 05-function-return.py
python 06-addition-function.py
python 07-salary-calculator.py
python 08-cloud-cost.py
python 09-kubernetes-health.py
python 10-devops-monitor.py
```

---

## Learning Outcome

After completing this lesson, you will be able to:

- Create functions using `def`
- Call functions multiple times
- Pass data using parameters
- Return values using `return`
- Build reusable Python code
- Organize programs into smaller logical units
- Combine functions with loops and conditional statements
- Write cleaner and more maintainable programs
- Apply functions in DevOps automation scripts

---

## Real-World Usage

Functions are used in almost every software application and automation platform.

### DevOps

- Infrastructure Automation
- Deployment Scripts
- Health Check Automation
- Monitoring Scripts
- Log Processing
- Backup Automation

### Cloud

- AWS Resource Provisioning
- Azure Automation
- GCP Automation
- Cost Calculation
- EC2 Management
- S3 Operations

### Kubernetes

- Pod Health Checks
- Cluster Monitoring
- Deployment Validation
- Namespace Management

### Backend Development

- API Endpoints
- Authentication
- Database Operations
- Business Logic
- Data Validation

---

## Built-in Python Functions

Python already provides many built-in functions.

Examples:

```python
print()

input()

len()

type()

range()

int()

float()

str()

sum()

max()

min()
```

You can also create your own custom functions using the `def` keyword.

---

## Key Takeaways

- Functions help write reusable code.
- A function executes only when it is called.
- Parameters allow functions to accept input.
- `return` sends data back to the caller.
- Functions make programs modular and easier to maintain.
- Every large Python application consists of many small reusable functions.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation