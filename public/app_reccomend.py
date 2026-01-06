from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load the trained Random Forest model
model = joblib.load('D:/pbl2.0/pbl2.0/farm/public/RandomForest.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract features from the data
        features = [
            data['nitrogen'],
            data['phosphorus'],
            data['potassium'],
            data['temperature'],
            data['humidity'],
            data['ph'],
            data['rainfall']
        ]

        # Make a prediction
        prediction = model.predict([features])

        # Return the prediction as JSON
        return jsonify({'recommendedCrop': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
