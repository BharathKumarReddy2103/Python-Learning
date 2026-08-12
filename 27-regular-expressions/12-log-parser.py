import re

log = "2026-08-12 19:30:45 ERROR Database connection failed"

pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (\w+) (.+)"

match = re.search(pattern, log)

if match:
    level = match.group(1)
    message = match.group(2)

    print("Log Level:", level)
    print("Message:", message)
else:
    print("Log format not recognized")