
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return jsonify({
        "message": "Kubernetes Demo Application is Running!",
        "application": "Self-Healing and Auto-Scaling Demo",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "hostname": socket.gethostname()
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/ready")
def readiness():
    return jsonify({
        "status": "ready"
    }), 200


@app.route("/info")
def info():
    return jsonify({
        "application": "Kubernetes Demo",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "pod": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
