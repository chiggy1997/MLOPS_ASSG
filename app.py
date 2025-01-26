from flask import Flask, request, jsonify
import joblib
import numpy as np


# Load the model
model = joblib.load('svm.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running inside Docker!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)