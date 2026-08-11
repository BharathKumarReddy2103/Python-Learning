def check_build(status):
    if status == "success":
        print("Build Successful")
    else:
        print("Build Failed")


def check_tests(status):
    if status == "success":
        print("Tests Passed")
    else:
        print("Tests Failed")