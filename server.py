from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Diccionario para traducir la emoción dominante final
    traduccion = {
        'anger': 'ira',
        'disgust': 'asco',
        'fear': 'miedo',
        'joy': 'alegría',
        'sadness': 'tristeza'
    }
    emocion_traducida = traduccion.get(response['dominant_emotion'], response['dominant_emotion'])
    
    return f"Para la declaración dada, la respuesta del sistema es 'ira': {response['anger']}, 'asco': {response['disgust']}, 'miedo': {response['fear']}, 'alegría': {response['joy']} y 'tristeza': {response['sadness']}. La emoción dominante es {emocion_traducida}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)