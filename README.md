# manage_kubernetes_pods
RBAC roles
kubectl create -f roles.yaml
kubectl auth reconcile -f my_role_binding.yaml
good resources on using kubernetes API - https://betterprogramming.pub/automate-all-the-boring-kubernetes-operations-with-python-7a31bbf7a387
POD Creation example - https://github.com/kubernetes-client/python/blob/master/examples/pod_exec.py
API Documentation - https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md
