from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend rodando no Render!"

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})
