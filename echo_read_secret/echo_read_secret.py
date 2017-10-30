import base64
from flask import request, jsonify
from kubernetes import config, client


def main():
    input = request.json

    # This requires a secret to exist in the environment
    #     kubectl create secret generic echo --from-literal=content=foobar
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    for secrets in v1.list_secret_for_all_namespaces().items:
        if secrets.metadata.name == 'echo':
            content = base64.b64decode(secrets.data['content'])
            output = {'input': input, 'secret': content.decode('utf-8')}
            return jsonify(output)
