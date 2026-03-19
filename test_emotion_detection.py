from flask import Flask, request, jsonify
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    data = request.get_json()

    text = data.get("text")

    result = emotion_detector(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)