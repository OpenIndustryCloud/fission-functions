from flask import request, jsonify


def main():
    input = request.json
    return jsonify(input)

# This is a useless comment to test PR