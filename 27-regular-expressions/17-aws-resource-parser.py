import re

output = """
EC2 Instance: i-1234567890abcdef0
S3 Bucket: production-backups
RDS Instance: roboshop-db
EKS Cluster: production-eks
"""

ec2 = re.search(r"EC2 Instance:\s*(i-[a-f0-9]+)", output)
s3 = re.search(r"S3 Bucket:\s*([a-z0-9-]+)", output)
rds = re.search(r"RDS Instance:\s*([a-z0-9-]+)", output)
eks = re.search(r"EKS Cluster:\s*([a-z0-9-]+)", output)

if ec2:
    print("EC2:", ec2.group(1))

if s3:
    print("S3:", s3.group(1))

if rds:
    print("RDS:", rds.group(1))

if eks:
    print("EKS:", eks.group(1))