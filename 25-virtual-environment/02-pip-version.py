import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pip", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout.strip())