import pandas as pd
from src.config import TIMEZONE

VALUE_COLS = ["aqi", "pm25", "pm10", "temp", "humidity", "wind"]

def clean_readings(df):
    df = df.copy()
    for c in VALUE_COLS:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    
    df["observed_at"] = pd.to_datetime(df["observed_at"], utc=True).dt.tz_convert(TIMEZONE)
    df = df.drop_duplicates(["station_id", "observed_at"]).sort_values("observed_at")
    
    # Drop impossible values
    df.loc[~df["aqi"].between(0, 500), "aqi"] = float("nan")
    df.loc[~df["humidity"].between(0, 100), "humidity"] = float("nan")
    return df

def to_daily(df, min_hours=12):
    hourly = df.set_index("observed_at")[VALUE_COLS].resample("h").mean()
    enough = hourly["aqi"].resample("D").count() >= min_hours
    daily = hourly.resample("D").mean()
    daily.loc[~enough] = float("nan")
    return daily