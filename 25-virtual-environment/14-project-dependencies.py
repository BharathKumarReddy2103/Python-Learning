import sys
import requests

dependencies = {
    "Python": sys.version.split()[0],
    "Requests": requests.__version__
}

for name, version in dependencies.items():
    print(name, ":", version)