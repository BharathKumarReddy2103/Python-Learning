import re

log = """
Pipeline: roboshop
Build: 125
Tests: PASSED
Deployment: SUCCESS
"""

pipeline = re.search(r"Pipeline:\s*(\w+)", log)
build = re.search(r"Build:\s*(\d+)", log)
tests = re.search(r"Tests:\s*(\w+)", log)
deployment = re.search(r"Deployment:\s*(\w+)", log)

if pipeline:
    print("Pipeline:", pipeline.group(1))

if build:
    print("Build:", build.group(1))

if tests:
    print("Tests:", tests.group(1))

if deployment:
    print("Deployment:", deployment.group(1))

if re.search(r"Deployment:\s*SUCCESS", log):
    print("CI/CD deployment successful")
else:
    print("CI/CD deployment failed")