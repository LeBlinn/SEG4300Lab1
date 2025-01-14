from transformers import pipeline
from flask import Flask, request
import waitress

app = Flask(__name__)
pipe = pipeline("text-classification", model="ProsusAI/finbert")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    prediction = pipe(text)  
    return prediction

if __name__ == "__main__":
    print("Server starting...")
    waitress.serve(app, host='127.0.0.1', port=5000)