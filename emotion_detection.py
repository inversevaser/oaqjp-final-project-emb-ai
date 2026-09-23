import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": {"text": text_to_analyze}}

    ret_resp = requests.post(url, json = obj, headers=header)
    format_resp = json.loads(ret_resp.text)

    anger = format_resp["emotionPredictions"][0]["emotion"]["anger"]
    disgust = format_resp["emotionPredictions"][0]["emotion"]["disgust"]
    fear = format_resp["emotionPredictions"][0]["emotion"]["fear"]
    joy = format_resp["emotionPredictions"][0]["emotion"]["joy"]
    sadness = format_resp["emotionPredictions"][0]["emotion"]["sadness"]
    dominant_emotion_num = max([anger,disgust,fear,joy,sadness])

    if dominant_emotion_num == anger:
        dominant_emotion = "anger"
    elif dominant_emotion_num == disgust:
        dominant_emotion = "disgust"
    elif dominant_emotion_num == joy:
        dominant_emotion = "joy"
    elif dominant_emotion_num == fear:
        dominant_emotion = "fear"
    else:
        dominant_emotion = "sadness"

    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy,
     'sadness': sadness, 'dominant_emotion': dominant_emotion}