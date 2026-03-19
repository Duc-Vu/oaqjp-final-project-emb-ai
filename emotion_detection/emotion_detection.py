import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

def emotion_detector(text):
    if not text:
        return {"error": "Invalid input"}

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    data = {
        "raw_document": {
            "text": text
        }
    }

    try:
        response = requests.post(URL, json=data, headers=headers)
        result = response.json()

        emotions = result["emotionPredictions"][0]["emotion"]

        dominant = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant
        }

    except Exception:
        return {"error": "API call failed"}