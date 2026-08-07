aws = {
    "web01",
    "db01"
}

azure = {
    "db01",
    "app01"
}

print(aws.difference(azure))