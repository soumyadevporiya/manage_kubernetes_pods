# manage_kubernetes_pods
RBAC roles - 
kubectl create -f roles.yaml
kubectl auth reconcile -f my_role_binding.yaml
good resources on using kubernetes API - https://betterprogramming.pub/automate-all-the-boring-kubernetes-operations-with-python-7a31bbf7a387
POD Creation example - https://github.com/kubernetes-client/python/blob/master/examples/pod_exec.py
API Documentation - https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md
Ephemeral POD - https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
Restart Policy - https://github.com/kubernetes-client/python/blob/master/kubernetes/client/models/v1_pod_spec.py
Container Creation  -  https://www.programcreek.com/python/example/96329/kubernetes.client.V1PodSpec
Kuberenetes Python API Object Hierarchy - https://github.com/kubernetes-client/python/blob/master/kubernetes/client/models/v1_pod_spec.py
