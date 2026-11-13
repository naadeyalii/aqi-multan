Multan AQI Prediction Engine

Enterprise-Grade Environmental Telemetry & Machine Learning Forecasting

A high-fidelity Data Science dashboard designed to predict next-day Air Quality Index (AQI) levels for Multan, Pakistan. Built to operate in intermittent network environments, this project features a hybrid live-API/offline-edge pipeline, a parametric machine learning model capable of extreme smog extrapolation, and a custom Dribbble-inspired UI.

🚀 Key Features

Real-Time API Ingestion: Automatically fetches live telemetry (AQI, PM2.5, PM10) from the World Air Quality Index (WAQI) for Multan station initialization.

Hybrid Edge Mode: Designed with manual telemetry fallbacks to ensure 100% operational uptime in restricted or offline university lab environments.

Extreme Event Extrapolation: Utilizes a custom-trained Parametric Ridge Regression model to accurately forecast unprecedented 500+ AQI smog spikes without "regression to the mean" flatlining.

AI Explainability: Dynamic, CSS/SVG-rendered interface that breaks down the mathematical feature weights (PM2.5, PM10, AQI persistence) driving the day's forecast.

Bento Grid UI: A fully custom, dark-matte aesthetic bypassing generic Streamlit components for a premium, enterprise-grade presentation.

🧠 Machine Learning Architecture

The Model: Ridge Regression (Parametric)

Initially prototyped with a Random Forest Regressor, the engine was upgraded to a Ridge Regression algorithm to handle Multan's severe winter smog variations.

The Problem with Random Forest: Tree-based models cannot extrapolate beyond the maximum value present in their historical training data (historical max: 302 AQI). During extreme smog events (e.g., 600+ AQI), the model artificially capped predictions.

The Solution: Ridge Regression learns the true mathematical relationship between pollutants, allowing the engine to scale forecasts infinitely alongside rising PM2.5/PM10 concentrations.

Current Validation MAE: 13.23 (Mean Absolute Error).

Feature Importance

The current model relies on the following weights to predict t+1 AQI:

PM2.5 Concentration: ~58.6% (Dominant Predictor)

Current AQI Persistence: ~32.4%

PM10 Concentration: ~9.0%

⚙️ Installation & Usage

Prerequisites

Python 3.9+

A World Air Quality Index (WAQI) API Token (Optional: gracefully falls back to offline mode without it).

1. Local Setup

Clone the repository and activate your virtual environment:

git clone https://github.com/naadeyalii/aqi-multan.git
cd aqi-multan
python -m venv .venv
.venv\Scripts\activate  # Windows


2. Install Dependencies

pip install -r requirements.txt


3. Run the Dashboard

To bypass strict Windows Application Control policies (often found on institutional or heavily secured laptops), launch the dashboard directly through the Python module:

python -m streamlit run app.py


📂 Project Structure

aqi-multan/
│
├── app.py                  # Main UI & Dashboard application
├── retrain.py              # ML script for training the Ridge Regression model
├── predict.py              # CLI testing script for model inference
│
├── data/
│   ├── raw/                # Raw API dumps and historical Kaggle datasets
│   └── processed/          # Cleaned, harmonized data ready for ML ingestion
│
├── models/
│   └── rf_aqi_model.joblib # Serialized Ridge Regression model weights
│
├── src/                    # Pipeline scripts (ingest.py, clean.py, pipeline.py)
└── requirements.txt        # Python package dependencies


Developed by: NAD E ALI MALIK.
