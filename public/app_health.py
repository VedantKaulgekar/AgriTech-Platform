from flask import Flask, request, jsonify
import tensorflow as tf
from flask_cors import CORS
import numpy as np

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Load the model
model = tf.keras.models.load_model('public/plant_health_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the frontend (POST request)
        data = request.get_json()

        # Feature list based on incoming data
        features = [
            data['soilMoisture'],
            data['ambientTemp'],
            data['soilTemp'],
            data['humidity'],
            data['lightIntensity'],
            data['soilPh'],
            data['nitrogen'],
            data['phosphorus'],
            data['potassium'],
            data['chlorophyll'],
            data['electrochemical'],
            25.0  # Default for leafTemp if not available
        ]

        # Convert features to numpy array and reshape
        input_features = np.array(features).reshape(1, -1)

        # Predict the health status using the model
        prediction = model.predict(input_features)

        # Debugging: print the prediction to understand the output
        print("Prediction probabilities:", prediction)  # See full probabilities

        # Get the predicted class (index of the highest probability)
        predicted_class = np.argmax(prediction)  # Index of the highest probability
        health_score = prediction[0][predicted_class]  # Probability of the predicted class

        # Debugging: Check the predicted class and corresponding score
        print("Predicted Class Index:", predicted_class)
        print("Health Score for Predicted Class:", health_score)

        # Map the predicted class to health status
        health_status = ["Good", "Poor", "Fair"][predicted_class]  # Adjust based on your model classes

        # Return the result as a JSON response
        return jsonify({
            'healthStatus': health_status,
            'healthScore': float(health_score)  # Convert to float for JSON serialization
        })

    except Exception as e:
        # Handle exceptions and return an error message
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
