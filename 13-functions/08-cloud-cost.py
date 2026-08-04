def total_cost(ec2, rds, s3):

    return ec2 + rds + s3

ec2 = float(input("EC2 Cost: "))
rds = float(input("RDS Cost: "))
s3 = float(input("S3 Cost: "))

cost = total_cost(ec2, rds, s3)

print("Monthly AWS Cost:", cost)