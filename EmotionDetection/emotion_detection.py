import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes text using Watson NLP Emotion Predict API.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"betamodel-id": "2022-04-01"}
    myobj = { "raw_document": { "content": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Xử lý lỗi khi input trống (Status code 400)
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Tìm cảm xúc có điểm số cao nhất
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
