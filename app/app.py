from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# -------------------------------
# App setup
# -------------------------------
app = Flask(__name__)
CORS(app)

# -------------------------------
# Load trained PIPELINE
# -------------------------------
pipeline = joblib.load("models/heart_risk_pipeline.pkl")

# -------------------------------
# Helper functions
# -------------------------------
def risk_category(prob):
    if prob < 0.3:
        return "Low risk"
    elif prob < 0.6:
        return "Medium risk"
    else:
        return "High risk"

# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    return "Heart Risk Estimator API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convert raw JSON → DataFrame
        input_df = pd.DataFrame([data])

        # 🔒 Force numeric conversion (critical)
        input_df = input_df.apply(pd.to_numeric, errors="coerce")

        # 🔒 Block invalid / missing inputs
        if input_df.isnull().any().any():
            return jsonify({
                "error": "Invalid input values. Please check all fields."
            }), 400

        # Pipeline handles preprocessing + model
        risk = pipeline.predict_proba(input_df)[0][1]

        return jsonify({
            "risk_score": round(float(risk), 3),
            "risk_level": risk_category(risk),
            "disclaimer": "Educational use only. Not medical advice."
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


    except Exception as e:
        return jsonify({"error": str(e)}), 400

# -------------------------------
# Run server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
