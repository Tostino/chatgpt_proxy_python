from flask import Blueprint, jsonify, request
from proxy import proxy

routes = Blueprint("routes", __name__)

@routes.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})

@routes.route("/api/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def api_proxy(path):
    return proxy(request, path)
