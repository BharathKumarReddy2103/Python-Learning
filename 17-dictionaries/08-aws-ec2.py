ec2 = {
    "InstanceId": "i-123456",
    "Region": "ap-south-1",
    "State": "Running",
    "Type": "t3.medium"
}

print("Instance :", ec2["InstanceId"])
print("Region   :", ec2["Region"])
print("State    :", ec2["State"])
print("Type     :", ec2["Type"])