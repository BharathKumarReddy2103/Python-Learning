# Virtual Environment

## Objective

Learn how to create and manage Python Virtual Environments, install and manage Python packages, maintain project dependencies, and build an isolated Python environment for DevOps automation.

Virtual environments are essential when building real-world Python applications because different projects may require different Python packages and package versions.

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
├── venv/
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