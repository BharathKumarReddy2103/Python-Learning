import sys
import os

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)
print("Working Directory:", os.getcwd())
print("Virtual Environment:", os.environ.get("VIRTUAL_ENV", "Not Active"))