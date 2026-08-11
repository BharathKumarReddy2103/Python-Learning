import aws_utils
import kubernetes_utils
import monitoring_utils
import cicd_utils

print("------ CI/CD ------")

cicd_utils.check_build("success")
cicd_utils.check_tests("success")

print("\n------ AWS ------")

aws_utils.check_ec2("i-123456")

print("\n------ Kubernetes ------")

kubernetes_utils.check_pod("frontend")

print("\n------ Monitoring ------")

monitoring_utils.check_cpu(70)
monitoring_utils.check_memory(75)