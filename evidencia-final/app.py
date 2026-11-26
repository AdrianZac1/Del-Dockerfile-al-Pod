
from flask import Flask, jsonify
from datetime import datetime, timezone
import socket

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify(
        nombre="Ángel Adrián Ávalos Zacarías",
        hora_servidor=datetime.now(timezone.utc).isoformat(),
        version="1.0",
        estado="operativo",
        host=socket.gethostname()
    )


@app.route("/healthz")
def healthz():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
