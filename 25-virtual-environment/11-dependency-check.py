import importlib.util

packages = [
    "requests"
]

for package in packages:
    if importlib.util.find_spec(package):
        print(package, ": Installed")
    else:
        print(package, ": Not Installed")