def validate_weather_data(data):
    required_fields = [
        "city",
        "latitude",
        "longitude",
        "temperature_f",
        "humidity_percent",
        "wind_speed_mph",
        "weather_code",
        "observation_time",
        "ingested_at",
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    if not 0 <= data["humidity_percent"] <= 100:
        raise ValueError(
            f"Invalid humidity: {data['humidity_percent']}"
        )

    if data["wind_speed_mph"] < 0:
        raise ValueError(
            f"Invalid wind speed: {data['wind_speed_mph']}"
        )

    return True