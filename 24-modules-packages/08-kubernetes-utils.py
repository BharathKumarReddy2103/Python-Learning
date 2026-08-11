import kubernetes_utils

kubernetes_utils.check_pod("frontend")
kubernetes_utils.check_namespace("production")