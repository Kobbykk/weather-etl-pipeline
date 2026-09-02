import pytest


@pytest.fixture
def valid_weather_data():
    return {
        "city": "Columbus",
        "latitude": 39.96841,
        "longitude": -82.98352,
        "temperature_f": 80.0,
        "humidity_percent": 50,
        "wind_speed_mph": 5.0,
        "weather_code": 0,
        "observation_time": "2026-09-01T20:00:00+00:00",
        "ingested_at": "2026-09-01T20:05:00+00:00",
    }