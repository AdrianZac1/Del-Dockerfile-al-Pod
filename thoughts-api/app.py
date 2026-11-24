from flask import Flask, jsonify
import os, socket
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        servicio="thoughts-api",
        version=os.environ.get("APP_VERSION", "sin-definir"),
        host=socket.gethostname(),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
