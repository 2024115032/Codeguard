from flask import Flask, request, jsonify
from services.analyzer import analyze_code
from services.review_service import review_pull_request

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


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json()

    if data.get("action") in ["opened", "synchronize"]:

        pull_request = data["pull_request"]
        repository = data["repository"]

        owner = repository["owner"]["login"]
        repo_name = repository["name"]
        pull_number = pull_request["number"]

        report = review_pull_request(
            owner,
            repo_name,
            pull_number
        )

        return jsonify({
            "status": "review completed",
            "report": report
        })

    return jsonify({
        "status": "ignored"
    })


if __name__ == "__main__":
    app.run(debug=True)