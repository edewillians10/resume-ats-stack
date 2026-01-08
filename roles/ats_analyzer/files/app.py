from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume = data.get("resume")
    job = data.get("job")

    if not resume or not job:
        return jsonify({"error": "resume and job are required"}), 400

    return jsonify({
        "score": 72,
        "missing_keywords": ["Kubernetes", "Terraform"],
        "suggestions": [
            "Add quantified achievements",
            "Match job title keywords"
        ]
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
