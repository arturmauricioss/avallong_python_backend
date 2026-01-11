from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permite requisições de qualquer origem

@app.route("/")
def home():
    return "Backend rodando no Render!"

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
