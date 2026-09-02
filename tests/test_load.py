from unittest.mock import patch

import psycopg
import pytest

from src.load import load_weather_data



@patch("src.load.psycopg.connect")
def test_load_weather_data_success(mock_connect):
    mock_connection = (
        mock_connect.return_value.__enter__.return_value
    )

    mock_cursor = (
        mock_connection.cursor.return_value.__enter__.return_value
    )

    weather_data = {
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

    load_weather_data(weather_data)

    mock_connect.assert_called_once()
    mock_connection.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once()

@patch("src.load.psycopg.connect")
def test_load_weather_data_database_failure(mock_connect):
    mock_connect.side_effect = psycopg.OperationalError(
        "Simulated database connection failure"
    )

    weather_data = {
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

    with pytest.raises(
        RuntimeError,
        match="Database load failed"
    ):
        load_weather_data(weather_data)