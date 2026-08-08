status = "  BUILD SUCCESSFUL  "

status = status.strip().lower()

if status == "build successful":
    print("Pipeline can continue")
else:
    print("Pipeline failed")