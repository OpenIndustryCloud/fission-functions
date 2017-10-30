import base64
from flask import request, jsonify
from kubernetes import config
config.load_incluster_config()
from kubernetes import client


def main():
    input = request.json

    # config.load_incluster_config()

    v1 = client.CoreV1Api()

    # This requires a secret to exist in the environment
    #     kubectl create secret generic echo --from-literal=content=foobar
    for secrets in v1.list_secret_for_all_namespaces().items:
        if secrets.metadata.name == 'echo':
            content = base64.b64decode(secrets.data['content'])

    output = {'input': input, 'secret': content}

    return jsonify(output)
