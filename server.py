from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/")
def index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def emotionDetector():
    text_analyzee = request.args.get("emotionPredictions")

    analyzed_response = emotion_detector(text_analyzee)

    final_response = "For the given statement, the system response is"
    for index, emoting in enumerate(list(analyzed_response.items)):
        if emoting[0] == "sadness":
            final_response += f"and {emoting[0]}:{emoting[1]}. "
        else:
            final_response += f"{emoting[0]}:{emoting[1]}, "
    final_response += "The dominant emotion is "
    final_response += f"{analyzed_response['dominant_emotion']}"
    return final_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
