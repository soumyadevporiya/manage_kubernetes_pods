import urllib.request
from flask import Flask
from flask import jsonify
import time
import json
from kafka import KafkaConsumer

# Required for Kubernetes
import os
import pint
import kubernetes
from kubernetes import client, config, watch
from kubernetes.client.models import V1PodSpec
from kubernetes.client.models import V1Container
from kubernetes.client.models import V1Pod
from kubernetes.client.models import V1ObjectMeta

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


# K8 Pod Details
@app.route('/hello/pods')
def get_pod_details():
    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    # v2 = kubernetes.client.V1Pod()
    # ret = v1.list_node()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    # details = " " + ret
    details = " "
    for i in ret.items:
        details = details + " " + i.status.pod_ip + " " + i.metadata.namespace + " " + i.metadata.name + "\n"

    return jsonify({"message": "POD Details ", "Information: ": details})


# K8 Pod Details
@app.route('/hello/readpod')
def get_readpod():
    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    # podspec_obj = kubernetes.client.V1Pod()
    # ret = v1.list_node()
    name = 'dataflowpod'
    namespace = 'default'
    ret = v1.read_namespaced_pod(name, namespace)

    if ret:
        details = "Exists"

    return jsonify({"message": "POD Details ", "Information: ": details})


# K8 Pod Creation
@app.route('/hello/createpod')
def get_createpod():
    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()

    name = 'my-dataflow-pod'
    namespace = 'default'

    pod_manifest = {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': name
        },
        'spec': {
            'restart_policy': 'Never',
            'containers': [{
                'image': 'gcr.io/mimetic-parity-378803/dataflow_pipeline:latest',
                'name': 'data-flowcontainer'
            }]
        }
    }
    resp = v1.create_namespaced_pod(body=pod_manifest, namespace='default')
    while True:
        resp = v1.read_namespaced_pod(name=name, namespace='default')
        if resp.status.phase != 'Pending':
            break
        time.sleep(1)

    ret = v1.read_namespaced_pod(name, namespace)

    if ret:
        details = "Created"

    return jsonify({"message": "POD Details ", "Information: ": details})


# K8 Pod Creation
@app.route('/hello/createpodsecond')
def get_createpodsecond():
    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()

    container_name = 'data-flowcontainer'
    namespace = 'default'
    pod_name = 'my-dataflow-pod'

    image = 'gcr.io/mimetic-parity-378803/dataflow_pipeline:latest'
    container = V1Container(name=container_name, image=image)
    podspec = V1PodSpec(containers=[container], restart_policy="Never")
    metadata = V1ObjectMeta(name=pod_name, namespace=namespace)
    pod = V1Pod(api_version='v1', kind='Pod', metadata=metadata, spec=podspec)

    my_pod = v1.create_namespaced_pod(namespace, pod)

    while True:
        resp = v1.read_namespaced_pod(name=pod_name, namespace='default')
        if resp.status.phase != 'Pending':
            break
        time.sleep(1)

    ret = v1.read_namespaced_pod(pod_name, namespace)

    if ret:
        details = "Created"

    return jsonify({"message": "POD Details ", "Information: ": details})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=60, threaded=True)
