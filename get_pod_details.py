import urllib.request
from flask import Flask
from flask import jsonify
import json
from kafka import KafkaConsumer

# Required for Kubernetes
import os
import pint
import kubernetes
from kubernetes import client, config, watch

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'



# K8 Pod Details
@app.route('/hello/pods')
def get_pod_details():
    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    #v2 = kubernetes.client.V1Pod()
    #ret = v1.list_node()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    #details = " " + ret
    details = " "
    for i in ret.items:
        details = details + " " + i.status.pod_ip+ " " + i.metadata.namespace + " " + i.metadata.name + "\n"

    return jsonify({"message":"POD Details ", "Information: ": details})

# K8 Pod Details
@app.route('/hello/readpod')
def get_readpod():
    config.load_incluster_config()
    v1 = kubernetes.client.CoreV1Api()
    #podspec_obj = kubernetes.client.V1Pod()
    #ret = v1.list_node()
    name = 'dataflowpod'
    namespace = 'default'
    ret = v1.read_namespaced_pod(name, namespace)

    details = " "

    details = details + " " + ret + "\n"

    return jsonify({"message":"POD Details ", "Information: ": details})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=60, threaded=True)
