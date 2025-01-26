from flask import Flask, request, jsonify
import joblib
import numpy as np
from gevent.pywsgi import WSGIServer


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

@app.route('/api', methods=['GET'])
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
