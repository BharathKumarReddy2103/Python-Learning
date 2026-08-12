import re

config = """
environment=production
region=ap-south-1
platform=eks
"""

environment = re.search(r"environment=(\w+)", config)
region = re.search(r"region=([a-z0-9-]+)", config)
platform = re.search(r"platform=(\w+)", config)

if environment:
    print("Environment:", environment.group(1))

if region:
    print("Region:", region.group(1))

if platform:
    print("Platform:", platform.group(1))