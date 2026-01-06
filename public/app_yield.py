from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

# Load your pre-trained scikit-learn model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "crop_yield_model.joblib")
# Load the trained model (including preprocessing pipeline)
model = joblib.load(MODEL_PATH)
import pandas as pd
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        # Parse and normalize input
        df = pd.DataFrame([{
            "Region": data.get("region", "").capitalize(),
            "Soil_Type": data.get("soiltype", "").capitalize(),
            "Crop": data.get("crop", "").capitalize(),
            "Rainfall_mm": float(data.get("rainfall", 0)),
            "Temperature_Celsius": float(data.get("temperature", 0)),
            "Fertilizer_Used": 1 if str(data.get("fertilizer", "false")).lower() == "true" else 0,
            "Irrigation_Used": 1 if str(data.get("irrigation", "false")).lower() == "true" else 0,
            "Weather_Condition": data.get("weather", "").capitalize(),
            "Days_to_Harvest": int(data.get("days_to_harvest", 0))
        }])

        # Ensure column order & names are what the model expects
        expected_cols = ['Region', 'Soil_Type', 'Crop', 'Rainfall_mm', 'Temperature_Celsius',
                         'Fertilizer_Used', 'Irrigation_Used', 'Weather_Condition', 'Days_to_Harvest']
        if not set(expected_cols).issubset(df.columns):
            return jsonify({"error": f"Missing required columns: {set(expected_cols) - set(df.columns)}"}), 400

        # Make prediction
        pred = model.predict(df)[0]
        return jsonify({"predicted_yield": round(float(pred), 2)})

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 400




if __name__ == "__main__":
    app.run(debug=True)
