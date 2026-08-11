from devops import aws
from devops import kubernetes
from devops import monitoring
from devops import cicd


print("------ CI/CD ------")

cicd.check_build("success")
cicd.check_tests("success")


print("\n------ AWS ------")

aws.check_ec2("i-123456")
aws.check_s3("production-backups")


print("\n------ Kubernetes ------")

kubernetes.check_pod("frontend")
kubernetes.check_namespace("production")


print("\n------ Monitoring ------")

monitoring.check_cpu(70)
monitoring.check_memory(85)