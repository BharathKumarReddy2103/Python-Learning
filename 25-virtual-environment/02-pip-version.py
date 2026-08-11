import subprocess

result = subprocess.run(
    ["python", "-m", "pip", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)