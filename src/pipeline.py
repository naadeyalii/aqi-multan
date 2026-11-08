import pandas as pd
from src.clean import clean_readings, to_daily
from src.config import RAW_PATH

def load_daily(station, path=RAW_PATH):
    raw = pd.read_csv(path, dtype={"station_id": str})
    raw = raw[raw["station_id"] == station]
    return to_daily(clean_readings(raw))