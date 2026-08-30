from datetime import datetime, timezone


def transform_weather_data(raw_data):
    current = raw_data["current"]

    transformed_data = {
        "city": "Columbus",
        "latitude": raw_data["latitude"],
        "longitude": raw_data["longitude"],
        "temperature_f": current["temperature_2m"],
        "humidity_percent": current["relative_humidity_2m"],
        "wind_speed_mph": current["wind_speed_10m"],
        "weather_code": current["weather_code"],
        "observation_time": datetime.fromisoformat(
            current["time"]
        ).replace(tzinfo=timezone.utc),
        "ingested_at": datetime.now(timezone.utc),
    }

    return transformed_data