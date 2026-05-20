import requests
import json

def emotion_detector(text_to_analyse):
    # Definimos la URL exacta de la Inteligencia Artificial de Watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Definimos la cabecera con el modelo que nos pide el proyecto
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Preparamos el texto que nos pasen para que Watson lo entienda
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Enviamos la petición a Internet y guardamos la respuesta
    response = requests.post(url, json=myobj, headers=header)
    
    # Devolvemos el texto tal cual nos lo manda Watson
    return response.text