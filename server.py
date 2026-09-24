""" imports flask and others"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/")
def index_page():
    """return with index page"""
    return render_template('index.html')


@app.route("/emotionDetector", methods=['GET'])
def emotion_detectors():
    """returning text string from emotion_detector onto the web page"""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    final_response = "For the given statement, the system response is "
    final_response += f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    final_response += f"'fear': {response['fear']}, 'joy': {response['joy']} "
    final_response += f"and 'sadness': {response['sadness']}. "
    final_response += f"The dominant emotion is {response['dominant_emotion']}."
    return final_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

