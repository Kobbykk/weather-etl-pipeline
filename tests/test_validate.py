import pytest

from src.validate import validate_weather_data


def create_valid_weather_data():
    return {
        "city": "Columbus",
        "latitude": 39.96841,
        "longitude": -82.98352,
        "temperature_f": 80.0,
        "humidity_percent": 50,
        "wind_speed_mph": 5.0,
        "weather_code": 0,
        "observation_time": "2026-08-31T20:00:00+00:00",
        "ingested_at": "2026-08-31T20:05:00+00:00",
    }


def test_valid_weather_data():
    data = create_valid_weather_data()

    assert validate_weather_data(data) is True


def test_invalid_humidity():
    data = create_valid_weather_data()
    data["humidity_percent"] = 150

    with pytest.raises(ValueError, match="Invalid humidity"):
        validate_weather_data(data)


def test_negative_wind_speed():
    data = create_valid_weather_data()
    data["wind_speed_mph"] = -10

    with pytest.raises(ValueError, match="Invalid wind speed"):
        validate_weather_data(data)


def test_missing_required_field():
    data = create_valid_weather_data()
    del data["temperature_f"]

    with pytest.raises(ValueError, match="Missing required field"):
        validate_weather_data(data)