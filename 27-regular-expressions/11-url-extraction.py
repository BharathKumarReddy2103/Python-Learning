import re

text = """
Documentation: https://kubernetes.io
API: https://api.example.com
Dashboard: https://grafana.example.com
"""

urls = re.findall(r"https?://[^\s]+", text)

for url in urls:
    print(url)