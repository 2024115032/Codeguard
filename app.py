from flask import Flask, request, jsonify
from services.analyzer import analyze_code

app = Flask(__name__)


@app.route("/")
def home():
    return "CodeGuard API is running!"


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    code = data.get("code", "")

    result = analyze_code(code)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)