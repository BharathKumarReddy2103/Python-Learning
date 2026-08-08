# File Handling

## Objective

Learn how to work with files in Python, including creating, reading, writing, appending, checking file existence, and processing file contents. File handling is an essential Python skill for DevOps automation, log processing, configuration management, inventory generation, reporting, and deployment automation.

---

## Why File Handling Matters

DevOps automation frequently requires scripts to read, modify, generate, and analyze files.

Examples include:

- Linux configuration files
- Application logs
- Kubernetes logs
- Server inventory files
- CI/CD reports
- Deployment configuration
- Environment configuration
- AWS resource information
- Docker and Kubernetes configuration
- Automation-generated reports

Python provides built-in file handling capabilities that allow automation scripts to work with these files efficiently.

---

## Concepts Covered

- Creating files
- Writing data to files
- Reading files
- Reading a single line
- Reading multiple lines
- Appending data
- Using `with open()`
- File modes
- Writing multiple lines
- Checking whether a file exists
- Processing log files
- Generating server inventories
- Generating Kubernetes configuration
- Generating CI/CD reports
- Reading and processing file contents

---

## File Modes

Python provides several file modes for working with files:

| Mode | Description |
|---|---|
| `r` | Read an existing file |
| `w` | Write to a file and overwrite existing content |
| `a` | Append data to an existing file |
| `x` | Create a new file |
| `r+` | Read and write |
| `w+` | Write and read |
| `a+` | Append and read |

Example:

    with open("servers.txt", "r") as file:
        data = file.read()

    print(data)

Using `with open()` is recommended because Python automatically closes the file after the operation is completed.

---

## Project Structure

    22-file-handling/
    │
    ├── 01-create-file.py
    ├── 02-write-file.py
    ├── 03-read-file.py
    ├── 04-readline.py
    ├── 05-readlines.py
    ├── 06-append-file.py
    ├── 08-with-open.py
    ├── 09-devops-log.py
    ├── 11-kubernetes-log.py
    ├── 12-file-modes.py
    ├── 13-write-multiple-lines.py
    ├── 14-file-exists.py
    ├── 15-devops-log-analyzer.py
    ├── 16-server-inventory.py
    ├── 17-kubernetes-config.py
    ├── 18-cicd-report.py
    │
    ├── server.txt
    ├── servers.txt
    ├── kubernetes.log
    ├── devops.log
    ├── file-modes.txt
    ├── inventory.txt
    ├── kubernetes-config.txt
    ├── deployment-report.txt
    │
    └── README.md

---

## Script Overview

### 01-create-file.py

Creates a new file using Python file handling.

Example:

    file = open("example.txt", "x")
    file.close()

---

### 02-write-file.py

Writes data into a file using write mode.

Example:

    with open("server.txt", "w") as file:
        file.write("web01")

---

### 03-read-file.py

Reads the complete contents of a file.

Example:

    with open("server.txt", "r") as file:
        data = file.read()

    print(data)

---

### 04-readline.py

Reads one line from a file.

Example:

    with open("servers.txt", "r") as file:
        line = file.readline()

    print(line)

---

### 05-readlines.py

Reads all lines from a file and returns them as a list.

Example:

    with open("servers.txt", "r") as file:
        lines = file.readlines()

    print(lines)

---

### 06-append-file.py

Adds new content to an existing file without removing the existing content.

Example:

    with open("servers.txt", "a") as file:
        file.write("\nredis01")

---

### 08-with-open.py

Demonstrates the recommended `with open()` approach for safe file handling.

Example:

    with open("servers.txt", "r") as file:
        for server in file:
            print(server.strip())

---

### 09-devops-log.py

Creates a DevOps-related log file containing deployment information.

Example output:

    INFO: Deployment started
    INFO: Docker image pulled
    INFO: Kubernetes deployment started
    INFO: Deployment completed successfully

---

### 11-kubernetes-log.py

Reads a Kubernetes log file and checks whether an `ERROR` message exists.

Example:

    if "ERROR" in logs:
        print("Kubernetes Error Found")
    else:
        print("Kubernetes Logs Healthy")

This demonstrates a simple approach to automated Kubernetes log analysis.

---

### 12-file-modes.py

Demonstrates different file modes such as writing and appending data.

The script demonstrates how existing file content can be replaced or additional configuration can be added.

---

### 13-write-multiple-lines.py

Creates a file containing multiple server entries.

Example output:

    web01
    web02
    db01
    redis01

---

### 14-file-exists.py

Checks whether a file exists before attempting to access it.

Example:

    import os

    if os.path.exists("servers.txt"):
        print("File exists")
    else:
        print("File does not exist")

Checking file existence helps prevent unnecessary file-related errors in automation scripts.

---

### 15-devops-log-analyzer.py

Reads a DevOps log file and analyzes the deployment status.

This demonstrates how Python can be used to automate basic log analysis and determine whether a deployment completed successfully.

---

### 16-server-inventory.py

Generates a server inventory file containing infrastructure information.

Example:

    web01
    web02
    db01
    redis01

This type of automation can be useful for infrastructure documentation, configuration management, and deployment automation.

---

### 17-kubernetes-config.py

Generates a Kubernetes configuration file containing cluster-related configuration.

Example:

    Cluster: production
    Namespace: default
    Platform: Kubernetes

---

### 18-cicd-report.py

Generates a CI/CD deployment report containing application, environment, platform, status, and container image information.

Example:

    CI/CD Deployment Report
    -----------------------
    Application: Roboshop
    Environment: Production
    Platform: Kubernetes
    Status: Successful
    Image: roboshop/frontend:1.0

---

## Real-World Applications

- Process Linux command output
- Analyze application logs
- Analyze Kubernetes logs
- Generate server inventories
- Create deployment reports
- Manage configuration files
- Generate CI/CD reports
- Process AWS resource information
- Generate Docker and Kubernetes configuration
- Check whether required files exist
- Append deployment information to log files
- Generate infrastructure documentation
- Build DevOps automation scripts

---

## Example: Kubernetes Log Analysis

A Python script can read Kubernetes logs and detect errors automatically.

Example:

    with open("kubernetes.log", "r") as file:
        logs = file.read()

    if "ERROR" in logs:
        print("Kubernetes Error Found")
    else:
        print("Kubernetes Logs Healthy")

This basic concept can later be extended to:

- Detect `CrashLoopBackOff`
- Detect `ImagePullBackOff`
- Detect failed deployments
- Count errors
- Generate alerts
- Create automated reports

---

## Example: Server Inventory Generation

Python can generate infrastructure inventory files automatically.

Example:

    servers = [
        "web01",
        "web02",
        "db01",
        "redis01"
    ]

    with open("inventory.txt", "w") as file:
        for server in servers:
            file.write(server + "\n")

    print("Inventory created")

This type of automation can be useful for:

- Ansible inventories
- Infrastructure documentation
- Server discovery
- Deployment automation
- Configuration management

---

## Important Learning Point

When running Python scripts that use relative file paths such as:

    open("servers.txt", "r")

Python looks for the file relative to the current working directory.

For example:

    Python-Learning/
    └── 22-file-handling/
        ├── 04-readline.py
        └── servers.txt

If the terminal is currently inside `22-file-handling`, the script can access:

    open("servers.txt", "r")

If the script is executed from another directory, Python may return:

    FileNotFoundError

This is an important concept when building real-world automation scripts.

---

## Common File Handling Errors

### FileNotFoundError

Occurs when Python cannot find the requested file.

Example:

    with open("servers.txt", "r") as file:
        data = file.read()

If `servers.txt` does not exist in the expected location, Python raises:

    FileNotFoundError

---

### PermissionError

Occurs when the Python process does not have sufficient permissions to access a file.

This is particularly important when working with:

- Linux system files
- Protected configuration files
- Application directories
- Production infrastructure

---

### Important Practice

Always consider:

- Where the script is being executed
- Where the file is located
- Whether the file exists
- Whether the user has permission to access it
- Whether the file should be overwritten or appended

These considerations become increasingly important in production automation.

---

## Learning Outcome

After completing this lesson, you will be able to:

- Create files using Python
- Write data to files
- Read complete file contents
- Read individual lines
- Read multiple lines
- Append data to existing files
- Use `with open()` safely
- Understand common file modes
- Check whether files exist
- Process DevOps and Kubernetes logs
- Generate server inventory files
- Generate Kubernetes configuration files
- Generate CI/CD deployment reports
- Automate basic file-based infrastructure tasks

---

## DevOps Connection

File handling is one of the foundations of Python-based DevOps automation.

The skills learned in this lesson can later be combined with:

    Python
       │
       ├── File Handling
       │      ├── Configuration
       │      ├── Logs
       │      ├── Reports
       │      └── Inventory
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

These concepts will eventually be used to build practical DevOps automation tools.

---

## Next Lesson

**23 - Exception Handling**

Topics include:

- `try`
- `except`
- `else`
- `finally`
- Handling `FileNotFoundError`
- Handling invalid input
- Handling runtime errors
- Creating reliable automation scripts
- Preventing scripts from crashing unexpectedly

Exception handling is especially important in DevOps automation because scripts frequently interact with files, APIs, cloud services, operating systems, and external commands where failures can occur.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation