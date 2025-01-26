from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "ML Model Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json()

    # Ensure the input data is valid
    if not data or 'features' not in data:
        return jsonify({'error': 'Invalid input. Please provide "features" as a list.'}), 400

    # Convert features to a NumPy array
    features = np.array(data['features']).reshape(1, -1)

    # Make a prediction
    prediction = model.predict(features)

    # Return the result
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)