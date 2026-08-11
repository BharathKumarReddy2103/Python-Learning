import subprocess

result = subprocess.run(
    ["python", "-m", "pip", "list"],
    capture_output=True,
    text=True
)

print(result.stdout)