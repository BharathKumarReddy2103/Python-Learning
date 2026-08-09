# Exception Handling

## Objective

Learn how to handle errors and unexpected situations in Python using exception handling. Exception handling is essential for building reliable automation scripts that can safely work with files, user input, configurations, APIs, operating systems, cloud platforms, Kubernetes, and CI/CD systems.

---

## Why Exception Handling Matters

Real-world automation does not always execute successfully.

A script may encounter situations such as:

- A configuration file does not exist
- A file cannot be accessed
- User input is invalid
- A dictionary key is missing
- A value has an incorrect data type
- A deployment fails
- A required configuration is missing
- An invalid environment is provided
- A Kubernetes configuration is incomplete
- An external operation fails

Without exception handling, these failures can cause Python programs to terminate unexpectedly.

Exception handling allows automation scripts to detect failures, provide meaningful error messages, and continue or stop execution in a controlled way.

---

## Concepts Covered

- `try`
- `except`
- Specific exceptions
- Multiple `except` blocks
- `as` with exceptions
- `else`
- `finally`
- `raise`
- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `PermissionError`
- `KeyError`
- `RuntimeError`
- User input validation
- File error handling
- Configuration validation
- Kubernetes configuration validation
- CI/CD deployment validation

---

## Project Structure

    23-exception-handling/
    │
    ├── 01-basic-try-except.py
    ├── 02-zero-division.py
    ├── 03-value-error.py
    ├── 04-file-not-found.py
    ├── 05-multiple-exceptions.py
    ├── 06-except-as.py
    ├── 07-else.py
    ├── 08-finally.py
    ├── 09-raise.py
    ├── 10-custom-validation.py
    ├── 11-user-input.py
    ├── 12-safe-file-reader.py
    ├── 13-devops-config.py
    ├── 14-kubernetes-config.py
    ├── 15-cicd-deployment.py
    └── README.md

---

## Basic Exception Handling

The basic structure of exception handling is:

    try:
        # code that may fail

    except SomeException:
        # handle the error

Example:

    try:
        number = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")

The `try` block contains code that may generate an exception.

The `except` block handles the exception.

---

## `try` and `except`

The `try` block is used for code that may fail.

The `except` block is executed when an exception occurs.

Example:

    try:
        number = 10 / 0
    except:
        print("An error occurred")

Output:

    An error occurred

Using specific exception types is generally preferred over a generic `except`.

---

## Specific Exceptions

Python provides many built-in exception types.

Example:

    try:
        number = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")

Handling a specific exception makes the code easier to understand and troubleshoot.

---

## Multiple Exceptions

A program can handle different types of exceptions separately.

Example:

    try:
        number = int("python")
        result = 10 / number

    except ValueError:
        print("Invalid number")

    except ZeroDivisionError:
        print("Cannot divide by zero")

This allows different failures to produce different error messages.

---

## Exception Information Using `as`

Exception details can be stored in a variable using `as`.

Example:

    try:
        number = int("python")

    except ValueError as error:
        print("Error:", error)

This is useful when troubleshooting automation failures because the exception can provide additional information about what went wrong.

---

## `else`

The `else` block executes when the `try` block completes successfully.

Example:

    try:
        number = int("100")
        print(number)

    except ValueError:
        print("Invalid number")

    else:
        print("Conversion successful")

The execution flow is:

    try
     │
     ├── Error ──> except
     │
     └── Success ──> else

---

## `finally`

The `finally` block executes whether an exception occurs or not.

Example:

    try:
        file = open("server.txt", "r")
        print(file.read())

    except FileNotFoundError:
        print("File not found")

    finally:
        print("File operation completed")

`finally` is useful for cleanup operations.

It can be used when working with:

- Files
- Network connections
- Database connections
- Temporary resources
- Automation resources

---

## `raise`

The `raise` statement allows a program to deliberately generate an exception.

Example:

    environment = "development"

    if environment != "production":
        raise ValueError("Production environment required")

This is useful when a script needs to enforce a specific condition.

---

## Common Exceptions

| Exception | Typical Scenario |
|---|---|
| `FileNotFoundError` | Required file does not exist |
| `PermissionError` | Insufficient permissions |
| `ValueError` | Invalid value |
| `TypeError` | Incorrect data type |
| `KeyError` | Dictionary key is missing |
| `IndexError` | Invalid list index |
| `ZeroDivisionError` | Division by zero |
| `RuntimeError` | Runtime operation failure |
| `Exception` | Generic base exception |

---

## Script Overview

### 01-basic-try-except.py

Introduces the basic `try` and `except` structure.

---

### 02-zero-division.py

Demonstrates handling `ZeroDivisionError`.

---

### 03-value-error.py

Demonstrates handling `ValueError` when converting invalid data.

---

### 04-file-not-found.py

Demonstrates handling `FileNotFoundError` when a required file does not exist.

---

### 05-multiple-exceptions.py

Demonstrates handling multiple exception types using multiple `except` blocks.

---

### 06-except-as.py

Demonstrates how to capture exception information using `as`.

---

### 07-else.py

Demonstrates the `else` block that executes when the `try` block succeeds.

---

### 08-finally.py

Demonstrates the `finally` block that executes regardless of whether an exception occurs.

---

### 09-raise.py

Demonstrates manually raising an exception when a required condition is not satisfied.

---

### 10-custom-validation.py

Demonstrates validating DevOps configuration values and raising an exception when an invalid environment is provided.

---

### 11-user-input.py

Demonstrates handling invalid or empty user input.

---

### 12-safe-file-reader.py

Demonstrates safe file reading with `FileNotFoundError` and `PermissionError` handling.

---

### 13-devops-config.py

Demonstrates handling missing keys in a DevOps configuration dictionary.

---

### 14-kubernetes-config.py

Demonstrates validation and exception handling for Kubernetes configuration data.

---

### 15-cicd-deployment.py

Demonstrates validating CI/CD deployment information and raising an exception when a deployment fails.

---

## Real-World Applications

- Handle missing configuration files
- Process invalid user input
- Validate deployment configuration
- Handle Kubernetes configuration errors
- Handle missing dictionary keys
- Detect failed deployments
- Handle file access errors
- Prevent automation scripts from crashing unexpectedly
- Validate environment configuration
- Build reliable CI/CD automation
- Handle failures in infrastructure automation
- Provide meaningful error messages
- Implement controlled failure handling

---

## DevOps Example

Exception handling becomes particularly useful when automation scripts interact with infrastructure.

A deployment script may perform operations such as:

    Read configuration
          │
          ▼
    Validate configuration
          │
          ▼
    Read inventory
          │
          ▼
    Deploy application
          │
          ▼
    Validate deployment
          │
          ▼
    Generate report

Any of these operations can fail.

Exception handling allows the script to identify the failure and respond appropriately instead of terminating without useful information.

---

## Example: Safe Configuration Access

A DevOps configuration can be validated using exception handling.

Example:

    config = {
        "environment": "production",
        "region": "ap-south-1",
        "platform": "EKS"
    }

    try:
        environment = config["environment"]
        region = config["region"]
        platform = config["platform"]

        print("Environment :", environment)
        print("Region      :", region)
        print("Platform    :", platform)

    except KeyError as error:
        print("Missing configuration:", error)

This approach can be extended to larger infrastructure configuration systems.

---

## Example: Kubernetes Configuration

Python automation may process Kubernetes-related configuration.

Example:

    config = {
        "cluster": "production-eks",
        "namespace": "default",
        "deployment": "frontend"
    }

    try:
        cluster = config["cluster"]
        namespace = config["namespace"]
        deployment = config["deployment"]

        print("Cluster    :", cluster)
        print("Namespace  :", namespace)
        print("Deployment :", deployment)

    except KeyError as error:
        print("Kubernetes configuration missing:", error)

This provides controlled handling when required configuration values are missing.

---

## Example: CI/CD Deployment Validation

A deployment script can validate deployment status.

Example:

    deployment = {
        "application": "roboshop",
        "environment": "production",
        "status": "success"
    }

    try:
        status = deployment["status"]

        if status != "success":
            raise RuntimeError("Deployment failed")

        print("Deployment successful")

    except KeyError as error:
        print("Deployment configuration missing:", error)

    except RuntimeError as error:
        print("Deployment Error:", error)

This pattern can later be extended to real CI/CD pipelines.

---

## Important Learning Point

Exception handling should not be used to hide errors.

Bad practice:

    try:
        deploy_application()

    except:
        pass

This hides the failure and makes troubleshooting difficult.

Better practice:

    try:
        deploy_application()

    except RuntimeError as error:
        print("Deployment failed:", error)

Meaningful error handling makes automation easier to troubleshoot and maintain.

---

## Best Practices

- Handle specific exceptions when possible
- Avoid unnecessary generic `except` blocks
- Provide meaningful error messages
- Do not silently ignore failures
- Use `finally` for cleanup operations
- Use `raise` when invalid conditions must stop execution
- Validate configuration before performing operations
- Keep exception handling close to the operation that may fail
- Log important failures in production automation
- Fail safely when required infrastructure information is missing

---

## Learning Outcome

After completing this lesson, you will be able to:

- Understand Python exceptions
- Use `try` and `except`
- Handle specific exception types
- Handle multiple exceptions
- Capture exception information
- Use `else`
- Use `finally`
- Raise exceptions manually
- Validate user input
- Handle file-related failures
- Handle missing dictionary keys
- Validate DevOps configuration
- Handle Kubernetes configuration errors
- Validate CI/CD deployment status
- Build more reliable automation scripts

---

## DevOps Connection

Exception handling is a critical foundation for Python-based DevOps automation.

The skills learned in this lesson can later be combined with:

    Python
       │
       ├── Exception Handling
       │      ├── File Errors
       │      ├── Configuration Errors
       │      ├── Validation Errors
       │      └── Deployment Errors
       │
       ├── File Handling
       │
       ├── OS Automation
       │
       ├── Subprocess
       │
       ├── JSON / YAML
       │
       ├── APIs
       │
       ├── AWS
       │
       ├── Kubernetes
       │
       └── CI/CD Automation

These concepts will eventually be combined to build production-oriented DevOps automation tools.

---

## Next Lesson

**24 - Modules and Packages**

Topics include:

- Importing modules
- Creating custom modules
- Using built-in modules
- `import`
- `from ... import`
- Module aliases
- Reusable Python code
- Organizing automation code
- Creating reusable DevOps utilities

Modules and packages are important because real-world Python automation should be organized into reusable components instead of keeping all logic inside a single Python file.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation