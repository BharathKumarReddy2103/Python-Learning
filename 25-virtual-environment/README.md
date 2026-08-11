````markdown
# Virtual Environment

## Objective

Learn how to create and manage Python Virtual Environments, install and manage Python packages, maintain project dependencies, and build an isolated Python environment for DevOps automation.

---

## Why Virtual Environments Matter

A Python project may require specific versions of libraries.

For example:

- Project A may require `requests==2.34.2`
- Project B may require a different version of `requests`
- One project may require `boto3`
- Another project may require `kubernetes`
- Another project may require `PyYAML`

Installing everything globally can create dependency conflicts.

A virtual environment provides an isolated environment for each Python project.

This allows each project to manage its own:

- Python packages
- Package versions
- pip version
- Dependencies
- Development environment

---

## Concepts Covered

- Python version
- pip
- Virtual environments
- Creating a virtual environment
- Activating a virtual environment
- Deactivating a virtual environment
- Installing packages
- Upgrading pip
- Checking installed packages
- `pip list`
- `pip show`
- `pip freeze`
- `requirements.txt`
- Installing dependencies from `requirements.txt`
- Importing external packages
- Making API requests with `requests`
- Dependency validation
- Environment information
- DevOps automation dependencies
- Isolated project environments
- `.gitignore` for virtual environments

---

## Project Structure

```text
25-virtual-environment/
│
├── 01-python-version.py
├── 02-pip-version.py
├── 03-check-python.py
├── 04-installed-packages.py
├── 05-requirements.py
├── 06-import-requests.py
├── 07-api-request.py
├── 08-devops-dependency.py
├── 09-kubernetes-dependency.py
├── 10-aws-dependency.py
├── 11-dependency-check.py
├── 12-environment-info.py
├── 13-automation-environment.py
├── 14-project-dependencies.py
├── 15-devops-project.py
├── requirements.txt
├── .gitignore
└── README.md
````

---

## Virtual Environment Workflow

```text
Create Virtual Environment
          │
          ▼
      Activate
          │
          ▼
Install Dependencies
          │
          ▼
Run Python Application
          │
          ▼
Freeze Dependencies
          │
          ▼
requirements.txt
          │
          ▼
      Deactivate
```

---

## Creating a Virtual Environment

Create a virtual environment using:

```bash
python -m venv venv
```

This creates an isolated environment named:

```text
venv/
```

---

## Activating the Virtual Environment

For Git Bash on Windows:

```bash
source venv/Scripts/activate
```

After activation, the terminal displays:

```text
(venv)
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

---

## Verifying the Virtual Environment

Check which Python executable is being used:

```bash
which python
```

Expected:

```text
/d/Bharath/Python-Learning/25-virtual-environment/venv/Scripts/python
```

Check Python version:

```bash
python --version
```

Example:

```text
Python 3.13.4
```

Check pip:

```bash
python -m pip --version
```

Example:

```text
pip 26.2.1 from D:\Bharath\Python-Learning\25-virtual-environment\venv\Lib\site-packages\pip
```

The important point is that both Python and pip should come from the active virtual environment.

---

## Running Python Scripts

When `(venv)` is active, run Python scripts using:

```bash
python script.py
```

For example:

```bash
python 01-python-version.py
```

Do not explicitly use the system Python path:

```bash
C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe
```

because this bypasses the active virtual environment.

---

## 01 - Python Version

Learn how to identify:

* Python version
* Python executable path
* Python runtime information

Example:

```python
import sys

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)
```

---

## 02 - pip Version

Learn how to check the pip version associated with the active Python environment.

Recommended command:

```bash
python -m pip --version
```

Using `python -m pip` ensures that pip belongs to the Python interpreter currently being used.

---

## 03 - Check Python

Learn how to validate whether the installed Python version satisfies the project's requirements.

Example:

```python
import sys

if sys.version_info >= (3, 10):
    print("Python version is supported")
else:
    print("Python version is not supported")
```

---

## 04 - Installed Packages

Learn how to inspect packages installed inside the virtual environment.

```bash
python -m pip list
```

Example:

```text
Package            Version
------------------ -------
certifi            2026.7.22
charset-normalizer 3.4.9
idna               3.18
pip                26.2.1
requests           2.34.2
urllib3            2.7.0
```

---

## 05 - Requirements

Learn how to manage project dependencies using `requirements.txt`.

Example:

```text
requests==2.34.2
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## 06 - Import Requests

Learn how to install and import an external Python package.

Example:

```python
import requests

print("Requests version:", requests.__version__)
```

---

## 07 - API Request

Learn how Python can communicate with REST APIs using the `requests` library.

Example:

```python
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("API request successful")
```

---

## 08 - DevOps Dependency

Learn how external Python dependencies can be used in DevOps automation.

Examples:

* GitHub API
* REST APIs
* CI/CD systems
* Cloud APIs
* Monitoring APIs
* Deployment APIs

---

## 09 - Kubernetes Dependency

Python can be used for Kubernetes automation.

Examples include:

* Pod management
* Namespace management
* Deployment automation
* Resource validation
* Cluster automation

---

## 10 - AWS Dependency

Python is widely used for AWS automation.

Common libraries include:

* `boto3`
* `botocore`

Python can automate:

* EC2
* S3
* IAM
* VPC
* EKS
* RDS
* Lambda
* CloudWatch

---

## 11 - Dependency Check

Learn how to verify whether a required Python package is installed.

Example:

```python
import importlib.util

if importlib.util.find_spec("requests"):
    print("requests : Installed")
else:
    print("requests : Not Installed")
```

---

## 12 - Environment Information

Learn how to inspect the current Python execution environment.

Important information includes:

* Python version
* Python executable
* Working directory
* Virtual environment path

Example:

```python
import os
import sys

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)
print("Working Directory:", os.getcwd())
```

---

## 13 - Automation Environment

Combine Python and dependency information to validate a DevOps automation environment.

Example:

```text
DevOps Automation Environment
-----------------------------
Python: 3.13.4
Requests: 2.34.2
Virtual Environment: Active
```

---

## 14 - Project Dependencies

Learn how a Python project can validate its required dependencies.

Example:

```text
Python : 3.13.4
Requests : 2.34.2
```

Dependency validation is useful before running:

* Deployment scripts
* CI/CD automation
* Infrastructure automation
* API integrations
* Cloud automation

---

## 15 - DevOps Project

Combine the concepts from this lesson into a simple DevOps automation environment check.

Example:

```text
================================
 DevOps Automation Environment
================================
Python Version : 3.13.4
Requests       : 2.34.2
GitHub API     : Available
Environment    : Ready
```

---

## Installing Packages

Install a package:

```bash
python -m pip install requests
```

Install a specific version:

```bash
python -m pip install requests==2.34.2
```

Upgrade a package:

```bash
python -m pip install --upgrade requests
```

---

## Upgrading pip

Upgrade pip inside the active virtual environment:

```bash
python -m pip install --upgrade pip
```

Verify:

```bash
python -m pip --version
```

---

## Checking Installed Packages

List packages:

```bash
python -m pip list
```

Show information about a package:

```bash
python -m pip show requests
```

---

## Freeze Dependencies

Generate `requirements.txt`:

```bash
python -m pip freeze > requirements.txt
```

Example:

```text
certifi==2026.7.22
charset-normalizer==3.4.9
idna==3.18
requests==2.34.2
urllib3==2.7.0
```

---

## Install Dependencies From requirements.txt

A new environment can install all project dependencies using:

```bash
python -m pip install -r requirements.txt
```

This is commonly used in:

* Development environments
* CI/CD pipelines
* Docker builds
* Production deployments
* Automation servers

---

## Deactivating the Virtual Environment

When finished:

```bash
deactivate
```

The `(venv)` indicator disappears from the terminal.

---

## Git and Virtual Environments

Virtual environments should not normally be committed to Git.

Add the following to `.gitignore`:

```text
venv/
.venv/
env/
__pycache__/
*.pyc
```

Commit:

```text
requirements.txt
```

instead of the complete `venv/` directory.

Another developer can recreate the environment using:

```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
```

---

## Real-World DevOps Applications

Virtual environments are commonly used when building Python automation for:

* AWS automation
* Kubernetes automation
* Terraform automation
* CI/CD pipelines
* GitHub API automation
* Docker automation
* Monitoring automation
* Log processing
* Infrastructure automation
* Cloud API integrations
* Deployment automation

A typical DevOps Python project may use:

```text
DevOps Automation Project
          │
          ├── Python
          │
          ├── Virtual Environment
          │
          ├── requests
          │
          ├── boto3
          │
          ├── kubernetes
          │
          ├── PyYAML
          │
          └── requirements.txt
```

---

## Learning Outcome

After completing this lesson, you will be able to:

* Understand Python virtual environments
* Create isolated Python environments
* Activate and deactivate virtual environments
* Identify the active Python interpreter
* Identify the active pip installation
* Install Python packages
* Upgrade pip
* Check installed packages
* Inspect package information
* Create `requirements.txt`
* Install dependencies from `requirements.txt`
* Freeze project dependencies
* Validate Python environments
* Make API requests using `requests`
* Understand dependency isolation
* Prepare Python environments for DevOps automation
* Prevent virtual environments from being committed to Git

---

## Next Lesson

**26 - JSON Handling**

Topics include:

* JSON fundamentals
* JSON objects
* JSON arrays
* JSON strings
* JSON numbers
* `json.loads()`
* `json.dumps()`
* Reading JSON files
* Writing JSON files
* Parsing API responses
* Processing AWS API data
* Processing Kubernetes API data
* Converting JSON to Python dictionaries
* Converting Python dictionaries to JSON
* Working with nested JSON

JSON handling is an important Python skill because modern DevOps tools, cloud APIs, Kubernetes APIs, REST APIs, and automation systems frequently exchange data using JSON.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation

```
```
