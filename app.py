
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



