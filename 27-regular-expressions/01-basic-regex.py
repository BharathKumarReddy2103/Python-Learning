import re

text = "DevOps automation with Python"

pattern = "Python"

if re.search(pattern, text):
    print("Pattern found")
else:
    print("Pattern not found")