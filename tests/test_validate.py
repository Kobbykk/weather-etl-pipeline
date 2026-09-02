import pytest

from src.validate import validate_weather_data


def test_valid_weather_data(valid_weather_data):
    assert validate_weather_data(valid_weather_data) is True


def test_invalid_humidity(valid_weather_data):
    valid_weather_data["humidity_percent"] = 150

    with pytest.raises(ValueError, match="Invalid humidity"):
        validate_weather_data(valid_weather_data)


def test_negative_wind_speed(valid_weather_data):
    valid_weather_data["wind_speed_mph"] = -10

    with pytest.raises(ValueError, match="Invalid wind speed"):
        validate_weather_data(valid_weather_data)


def test_missing_required_field(valid_weather_data):
    del valid_weather_data["temperature_f"]

    with pytest.raises(ValueError, match="Missing required field"):
        validate_weather_data(valid_weather_data)