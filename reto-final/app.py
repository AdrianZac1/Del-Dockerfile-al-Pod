from flask import Flask, jsonify
import os, socket
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        servicio="reto-integrador",
        entorno=os.environ.get("ENTORNO", "sin-definir"),
        version="1.0",
        host=socket.gethostname(),
        estado="operativo"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
