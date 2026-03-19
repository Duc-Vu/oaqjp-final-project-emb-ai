from flask import Flask, request, render_template
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result=None)


@app.route("/emotionDetector")
def emotion_detector_api():
    text = request.args.get('textToAnalyze')

    response = emotion_detector(text)

    if "error" in response:
        result = "Invalid text! Please try again!"
    else:
        result = (
            f"For the given statement, the system response is "
            f"anger: {response['anger']}, "
            f"disgust: {response['disgust']}, "
            f"fear: {response['fear']}, "
            f"joy: {response['joy']} and "
            f"sadness: {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)