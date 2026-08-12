# Regular Expressions

## Objective

Learn the fundamentals of Python Regular Expressions using the built-in `re` module.

Regular Expressions, commonly called Regex, are used to search, match, extract, replace, validate, and analyze text patterns.

Regex is especially useful in DevOps automation for processing:

- Application logs
- Kubernetes logs
- CI/CD pipeline output
- AWS CLI output
- Server inventories
- Configuration files
- IP addresses
- URLs
- Email addresses
- Monitoring data
- Deployment information

---

## Why Regular Expressions Matter

DevOps engineers work with large amounts of text every day.

Examples include:

- Linux command output
- Application logs
- Kubernetes logs
- Docker logs
- AWS CLI output
- CI/CD pipeline logs
- Server inventories
- Configuration files
- Monitoring output
- API responses

Regular Expressions allow us to automate text processing instead of manually searching through large amounts of output.

For example, a log may contain:

```text
2026-08-12 19:30:45 ERROR Database connection failed
````

Regex can extract:

```text
ERROR
Database connection failed
```

This becomes extremely useful when building automation, monitoring, troubleshooting, and log-analysis scripts.

---

## Concepts Covered

* Importing the `re` module
* Basic regex patterns
* `re.search()`
* `re.match()`
* `re.findall()`
* `re.sub()`
* Character classes
* Quantifiers
* Groups
* IP address matching
* Email validation
* URL extraction
* Log parsing
* Kubernetes log analysis
* DevOps configuration parsing
* Server inventory parsing
* CI/CD log parsing
* AWS resource parsing
* DevOps log analysis

---

## Important Regex Symbols

### Character Classes

```text
[a-z]       Lowercase letters
[A-Z]       Uppercase letters
[0-9]       Digits
[a-zA-Z]    Letters
[^0-9]      Anything except digits
```

---

### Common Special Characters

```text
\d          Digit
\w          Word character
\s          Whitespace
.           Any character
^           Start of string
$           End of string
\b          Word boundary
```

---

### Quantifiers

```text
+           One or more
*           Zero or more
?           Zero or one
{n}         Exactly n occurrences
{n,}        n or more occurrences
{n,m}       Between n and m occurrences
```

---

## Project Structure

```text
27-regular-expressions/
│
├── 01-basic-regex.py
├── 02-re-search.py
├── 03-re-match.py
├── 04-re-findall.py
├── 05-re-sub.py
├── 06-character-classes.py
├── 07-quantifiers.py
├── 08-groups.py
├── 09-ip-address.py
├── 10-email-validation.py
├── 11-url-extraction.py
├── 12-log-parser.py
├── 13-kubernetes-log.py
├── 14-devops-config.py
├── 15-server-inventory.py
├── 16-cicd-log-parser.py
├── 17-aws-resource-parser.py
├── 18-devops-log-analyzer.py
└── README.md
```

---

# 01 - Basic Regex

File:

```text
01-basic-regex.py
```

Learn how to identify a basic text pattern using Regular Expressions.

Example:

```text
Pattern found
```

This is the foundation for all later regex operations.

---

# 02 - re.search()

File:

```text
02-re-search.py
```

Learn how to search for a pattern anywhere inside a string.

DevOps example:

```text
Pod found
```

This is useful when searching logs for:

* Pod names
* Error messages
* Deployment names
* Server names
* Resource names

---

# 03 - re.match()

File:

```text
03-re-match.py
```

Learn how `re.match()` checks whether a pattern appears at the beginning of a string.

Example:

```text
Error log detected
```

This can be useful when processing structured log entries where the beginning of the line has a known format.

---

# 04 - re.findall()

File:

```text
04-re-findall.py
```

Learn how to extract all matching values from a string.

Example:

```text
['web01', 'web02', 'db01']
```

This is extremely useful for extracting:

* Server names
* Pod names
* IP addresses
* Resource IDs
* URLs
* Log entries

---

# 05 - re.sub()

File:

```text
05-re-sub.py
```

Learn how to replace text using Regular Expressions.

Example:

```text
server=web01 environment=staging
```

Regex replacement can be used to modify:

* Configuration values
* Environment names
* Server names
* Log messages
* Deployment values

---

# 06 - Character Classes

File:

```text
06-character-classes.py
```

Learn how character classes can identify specific types of characters.

Example pattern:

```python
r"[a-z]+[0-9]+"
```

Example output:

```text
['web01', 'web02', 'db01']
```

The pattern identifies lowercase letters followed by digits.

This is useful for matching DevOps resource names such as:

```text
web01
web02
db01
redis123
```

---

# 07 - Quantifiers

File:

```text
07-quantifiers.py
```

Learn how quantifiers control how many times a pattern can occur.

Example:

```python
r"[a-z]+[0-9]+"
```

Example output:

```text
['web01', 'web02', 'db01', 'redis123']
```

Important quantifiers:

```text
+       One or more
*       Zero or more
?       Zero or one
{n}     Exactly n
{n,}    n or more
{n,m}   Between n and m
```

Quantifiers are commonly used when parsing:

* Server names
* Ports
* Resource IDs
* IP addresses
* Kubernetes resources
* Log values

---

# 08 - Groups

File:

```text
08-groups.py
```

Learn how regex groups allow us to extract different parts of a matching pattern.

Example input:

```text
web01:8080
```

Output:

```text
Server: web
Number: 01
Port: 8080
```

The pattern separates:

```text
web
01
8080
```

Groups are useful when parsing structured DevOps information.

---

# 09 - IP Address

File:

```text
09-ip-address.py
```

Learn how to extract an IPv4 address from text.

Example:

```text
Server IP: 192.168.1.100
```

Output:

```text
IP Address: 192.168.1.100
```

This technique can be useful for processing:

* Server inventories
* Network configuration
* Kubernetes node information
* Application logs
* Monitoring output

---

# 10 - Email Validation

File:

```text
10-email-validation.py
```

Learn how Regular Expressions can validate an email address.

Example:

```text
devops@example.com
```

Output:

```text
Valid email
```

Regex validation can be useful when processing:

* User input
* Configuration values
* Automation parameters
* Notification settings

---

# 11 - URL Extraction

File:

```text
11-url-extraction.py
```

Learn how to extract URLs from text.

Example input:

```text
Documentation: https://kubernetes.io
API: https://api.example.com
Dashboard: https://grafana.example.com
```

Output:

```text
https://kubernetes.io
https://api.example.com
https://grafana.example.com
```

This can be useful when processing:

* Application logs
* CI/CD output
* Monitoring notifications
* Documentation output
* API responses

---

# 12 - Log Parser

File:

```text
12-log-parser.py
```

Learn how to parse structured application logs.

Example:

```text
2026-08-12 19:30:45 ERROR Database connection failed
```

Output:

```text
Log Level: ERROR
Message: Database connection failed
```

Regex can extract:

* Date
* Time
* Log level
* Message
* Application name
* Error information

This is an important concept for log-processing automation.

---

# 13 - Kubernetes Log

File:

```text
13-kubernetes-log.py
```

Learn how to process Kubernetes logs and extract pod names.

Example:

```text
Pod frontend
Pod frontend
Pod backend
```

Output:

```text
Pods: ['frontend', 'frontend', 'backend']
Kubernetes error detected
```

The script also checks whether the log contains:

```text
ERROR
```

This demonstrates how regex can be used for basic Kubernetes log analysis.

---

# 14 - DevOps Configuration

File:

```text
14-devops-config.py
```

Learn how to extract configuration values from text.

Example configuration:

```text
environment=production
region=ap-south-1
platform=eks
```

Output:

```text
Environment: production
Region: ap-south-1
Platform: eks
```

This technique can be used when processing:

* Environment configuration
* Deployment configuration
* CI/CD variables
* Cloud configuration
* Infrastructure configuration

---

# 15 - Server Inventory

File:

```text
15-server-inventory.py
```

Learn how to parse server inventory information.

Example:

```text
web01 192.168.1.10
web02 192.168.1.11
db01 192.168.1.20
```

Output:

```text
Server: web01
IP: 192.168.1.10
Server: web02
IP: 192.168.1.11
Server: db01
IP: 192.168.1.20
```

This is useful for automation involving:

* Server inventories
* Infrastructure management
* Configuration management
* Network automation
* Monitoring systems

---

# 16 - CI/CD Log Parser

File:

```text
16-cicd-log-parser.py
```

Learn how to parse CI/CD pipeline information.

Example:

```text
Pipeline: roboshop
Build: 125
Tests: PASSED
Deployment: SUCCESS
```

Output:

```text
Pipeline: roboshop
Build: 125
Tests: PASSED
Deployment: SUCCESS
CI/CD deployment successful
```

This demonstrates how regex can be used to process:

* Pipeline names
* Build numbers
* Test status
* Deployment status
* CI/CD logs

---

# 17 - AWS Resource Parser

File:

```text
17-aws-resource-parser.py
```

Learn how to extract AWS resource information.

Example:

```text
EC2 Instance: i-1234567890abcdef0
S3 Bucket: production-backups
RDS Instance: roboshop-db
EKS Cluster: production-eks
```

Output:

```text
EC2: i-1234567890abcdef0
S3: production-backups
RDS: roboshop-db
EKS: production-eks
```

This demonstrates regex-based processing of AWS-related output.

Useful resources include:

* EC2 instance IDs
* S3 bucket names
* RDS identifiers
* EKS cluster names

---

# 18 - DevOps Log Analyzer

File:

```text
18-devops-log-analyzer.py
```

This is the final hands-on example for the lesson.

The script analyzes DevOps logs and counts different log levels.

Example:

```text
INFO: Deployment started
INFO: Docker image pulled
WARNING: High memory usage
ERROR: Kubernetes pod failed
INFO: Deployment completed
ERROR: Database connection failed
```

Output:

```text
INFO: 3
WARNING: 1
ERROR: 2
Critical errors detected
```

This demonstrates a practical DevOps use case for Regular Expressions.

The script can identify:

```text
INFO
WARNING
ERROR
```

and determine whether critical errors are present.

---

## Running the Scripts

From the lesson directory:

```bash
cd 27-regular-expressions
```

Run the scripts individually:

```bash
python 01-basic-regex.py
python 02-re-search.py
python 03-re-match.py
python 04-re-findall.py
python 05-re-sub.py
python 06-character-classes.py
python 07-quantifiers.py
python 08-groups.py
python 09-ip-address.py
python 10-email-validation.py
python 11-url-extraction.py
python 12-log-parser.py
python 13-kubernetes-log.py
python 14-devops-config.py
python 15-server-inventory.py
python 16-cicd-log-parser.py
python 17-aws-resource-parser.py
python 18-devops-log-analyzer.py
```

---

## Real-World DevOps Applications

Regular Expressions are useful for:

* Parsing Linux command output
* Analyzing application logs
* Analyzing Kubernetes logs
* Extracting Kubernetes pod names
* Processing Docker logs
* Parsing CI/CD pipeline output
* Extracting AWS resource IDs
* Processing server inventories
* Validating configuration values
* Extracting IP addresses
* Extracting URLs
* Validating email addresses
* Processing monitoring output
* Automating troubleshooting tasks
* Building log-analysis scripts

---

## Example DevOps Workflow

A typical automation workflow can look like:

```text
Log File
   │
   ▼
Read Log
   │
   ▼
Regular Expression
   │
   ├── Extract ERROR
   ├── Extract WARNING
   ├── Extract Pod Name
   ├── Extract IP Address
   └── Extract Resource ID
   │
   ▼
Analyze Results
   │
   ▼
Take Action
   │
   ├── Send Alert
   ├── Create Report
   ├── Trigger Automation
   └── Notify Engineer
```

---

## Learning Outcome

After completing this lesson, you will be able to:

* Understand Regular Expression fundamentals
* Use Python's `re` module
* Search for patterns using `re.search()`
* Match patterns using `re.match()`
* Extract multiple values using `re.findall()`
* Replace text using `re.sub()`
* Use character classes
* Use regex quantifiers
* Create regex groups
* Extract IP addresses
* Validate email addresses
* Extract URLs
* Parse application logs
* Analyze Kubernetes logs
* Parse DevOps configuration
* Process server inventories
* Parse CI/CD logs
* Extract AWS resource information
* Analyze DevOps logs
* Build practical regex-based automation scripts

---

## Key Takeaways

Regular Expressions are especially powerful when combined with other Python concepts learned earlier.

For example:

```text
Python Strings
      │
      ▼
String Methods
      │
      ▼
File Handling
      │
      ▼
Exception Handling
      │
      ▼
Modules and Packages
      │
      ▼
Virtual Environments
      │
      ▼
JSON Handling
      │
      ▼
Regular Expressions
      │
      ▼
DevOps Automation
```

Regex becomes much more useful when combined with:

* File handling
* JSON processing
* Exception handling
* Functions
* Modules
* Virtual environments
* API processing

These concepts together provide a strong foundation for building Python-based DevOps automation.

---

## Next Lesson

**28 - YAML Handling**

Topics will include:

* YAML fundamentals
* YAML syntax
* Reading YAML files
* Writing YAML files
* YAML dictionaries
* YAML lists
* Nested YAML
* Kubernetes YAML
* Configuration management
* DevOps configuration processing
* YAML automation with Python

YAML is heavily used in DevOps for Kubernetes manifests, CI/CD pipelines, configuration files, Ansible playbooks, and infrastructure automation.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Learning Software Development for DevOps Automation