import pandas as pd
from src.clean import clean_readings

def test_invalid_values_become_nan():
    df = pd.DataFrame({
        "station_id": ["s", "s"],
        "observed_at": ["2026-01-01T10:00:00+05:00", "2026-01-01T11:00:00+05:00"],
        "aqi": ["650", "120"], 
        "pm25": [1, 2], 
        "pm10": [1, 2],
        "temp": [10, 11], 
        "humidity": [50, 140], 
        "wind": [1, 1]
    })
    out = clean_readings(df)
    assert pd.isna(out["aqi"].iloc[0])  # 650 is outside 0-500, so it becomes NaN
    assert out["aqi"].iloc[1] == 120
    assert pd.isna(out["humidity"].iloc[1])  # 140% humidity is impossible, so it becomes NaN

def test_duplicates_removed():
    row = {
        "station_id": "s", 
        "observed_at": "2026-01-01T10:00:00+05:00",
        "aqi": 80, "pm25": 1, "pm10": 1, 
        "temp": 10, "humidity": 50, "wind": 1
    }
    out = clean_readings(pd.DataFrame([row, row]))
    assert len(out) == 1