import csv
import datetime as dt
import os
import requests
from dotenv import load_dotenv
from src.config import RAW_PATH, STATIONS

load_dotenv()
TOKEN = os.getenv("WAQI_TOKEN")
COLUMNS = ["station_id", "observed_at", "aqi", "pm25", "pm10", "temp", "humidity", "wind", "fetched_at"]

def fetch_station(station, token):
    r = requests.get(f"https://api.waqi.info/feed/{station}/", params={"token": token}, timeout=60)
    r.raise_for_status()
    payload = r.json()
    if payload.get("status") != "ok":
        raise RuntimeError(f"API error for {station}: {payload}")
    return payload["data"]

def to_row(station, data):
    iaqi = data.get("iaqi", {})
    get = lambda key: iaqi.get(key, {}).get("v")
    t = data["time"]
    observed = t.get("iso") or (t["s"].replace(" ", "T") + t.get("tz", "+05:00"))
    
    return {
        "station_id": station, "observed_at": observed, "aqi": data.get("aqi"),
        "pm25": get("pm25"), "pm10": get("pm10"), "temp": get("t"),
        "humidity": get("h"), "wind": get("w"),
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat()
    }

def append_row(row, path=RAW_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new_file = not os.path.exists(path)
    seen = set()
    if not new_file:
        with open(path, newline="") as f:
            seen = {(r["station_id"], r["observed_at"]) for r in csv.DictReader(f)}
    if (row["station_id"], row["observed_at"]) in seen:
        return False
        
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if new_file:
            writer.writeheader()
        writer.writerow(row)
    return True

def main():
    for station in STATIONS:
        try:
            added = append_row(to_row(station, fetch_station(station, TOKEN)))
            print(station, "added" if added else "already stored")
        except Exception as exc:
            print(station, "failed:", exc)

if __name__ == "__main__":
    main()