from flask import Flask, request, jsonify
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotion", methods=["POST"])
def detect_emotion():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    text = data["text"]

    result = emotion_detector(text)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)