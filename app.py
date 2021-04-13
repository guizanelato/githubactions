
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return jsonify(
            {
                'timestamp' : str(datetime.now()),
                'message': 'Hello, Github Actions!'

            })   


@app.route("/outra_rota", methods = ["GET"])
def outra_rota():
    return jsonify(
            {
                'timestamp': str(datetime.now()),
                'messagem': 'Adicionado outra funcionalidade no código'

            })
