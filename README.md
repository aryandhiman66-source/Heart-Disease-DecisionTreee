# Heart Disease Risk Estimator

An interpretable machine learning web application that estimates heart disease risk from clinical features using a pruned Decision Tree classifier. Built with scikit-learn, Flask, and a lightweight HTML/JS frontend.

## System Architecture

```
User Input (Web Form) → Flask API → ML Pipeline → Risk Score + Risk Level
```

### Components

| Component | Technology | Description |
|-----------|-----------|-------------|
| **Backend** | Flask (Python) | REST API with `/predict` endpoint |
| **Frontend** | HTML / CSS / JavaScript | Static form with 13 clinical inputs |
| **Model** | Decision Tree (scikit-learn) | Pruned with cost-complexity pruning |
| **Data** | Cleveland Heart Disease dataset | 303 patient records, 14 columns |

## Features

- **13 clinical inputs**: age, sex, chest pain type, blood pressure, cholesterol, fasting blood sugar, rest ECG, max heart rate, exercise-induced angina, ST depression (oldpeak), slope, number of major vessels (CA), thalassemia
- **Risk output**: probability score (0–1) and categorical risk level (Low / Medium / High)
- **Interpretable model**: Decision Tree chosen for transparency and auditability
- **Regularization**: cost-complexity pruning to prevent overfitting
- **Screening-focused evaluation**: prioritizes recall (sensitivity) over raw accuracy

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Install

```bash
pip install flask flask-cors joblib pandas scikit-learn
```

### Run

```bash
python app/app.py
```

The API starts at `http://127.0.0.1:5000`. Open `frontend/index.html` in a browser to use the UI.

### API Usage

**POST** `/predict`

```json
{
  "age": 55,
  "sex": 1,
  "cp": 0,
  "trestbps": 140,
  "chol": 240,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.2,
  "slope": 1,
  "ca": 0,
  "thal": 2
}
```

**Response:**

```json
{
  "risk_score": 0.42,
  "risk_level": "Medium risk",
  "disclaimer": "Educational use only. Not medical advice."
}
```

## Thresholds

| Risk Level | Probability Range |
|------------|------------------|
| Low risk | < 0.3 |
| Medium risk | 0.3 – 0.6 |
| High risk | > 0.6 |

## Project Structure

```
├── app/
│   └── app.py              # Flask API server
├── frontend/
│   └── index.html           # Web UI
├── models/
│   ├── heart_risk_pipeline.pkl  # Full sklearn pipeline
│   └── heart_risk_dt.pkl       # Raw decision tree model
├── heartdecisies.ipynb      # Training & experimentation notebook
├── processed.cleveland.data  # Heart disease dataset
└── README.md
```

## Limitations

- Trained on a benchmark dataset, not on real clinical population data
- Does not incorporate temporal or longitudinal patient information
- Risk thresholds are heuristic and not clinically validated
- **For educational and demonstration purposes only — not medical advice**

## Tech Stack

- Python, scikit-learn, Flask, joblib, NumPy, pandas
- Vanilla HTML, CSS, JavaScript
