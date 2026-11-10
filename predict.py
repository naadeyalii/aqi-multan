import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import joblib
import pandas as pd

# 1. Load your offline trained model
model = joblib.load('models/rf_aqi_model.joblib')

# 2. Input today's live sensor data 
# (You can change these numbers live during your presentation to show how the model reacts!)
todays_data = pd.DataFrame({
    'aqi': [160],     # Example: Today's AQI is High
    'pm25': [65.5],   # Example: High PM2.5
    'pm10': [90.2]    # Example: High PM10
})

# 3. Make the prediction for tomorrow
tomorrow_prediction = model.predict(todays_data)

print("\n--- MULTAN AQI PREDICTION SYSTEM (OFFLINE MODE) ---")
print(f"If Today's AQI is: {todays_data['aqi'][0]}")
print(f"Then PREDICTED AQI FOR TOMORROW IS: {tomorrow_prediction[0]:.0f}\n")