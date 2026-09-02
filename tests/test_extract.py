from unittest.mock import patch

import pytest
import requests

from src.extract import extract_weather_data


@patch("src.extract.requests.get")
def test_extract_weather_data_success(mock_get):
    fake_response = mock_get.return_value

    fake_response.json.return_value = {
        "latitude": 39.96841,
        "longitude": -82.98352,
        "current": {
            "temperature_2m": 80.0,
            "relative_humidity_2m": 50,
            "wind_speed_10m": 5.0,
            "weather_code": 0,
            "time": "2026-08-31T20:00",
        },
    }

    result = extract_weather_data()

    mock_get.assert_called_once()

    assert result["latitude"] == 39.96841
    assert result["current"]["temperature_2m"] == 80.0


@patch("src.extract.requests.get")
def test_extract_weather_data_failure(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError(
        "Simulated connection failure"
    )

    with pytest.raises(
        RuntimeError,
        match="Weather API request failed"
    ):
        extract_weather_data()