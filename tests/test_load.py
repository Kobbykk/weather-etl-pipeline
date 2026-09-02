from unittest.mock import patch

import psycopg
import pytest

from src.load import load_weather_data


@patch("src.load.psycopg.connect")
def test_load_weather_data_success(
    mock_connect,
    valid_weather_data,
):
    mock_connection = (
        mock_connect.return_value.__enter__.return_value
    )

    mock_cursor = (
        mock_connection.cursor.return_value.__enter__.return_value
    )

    load_weather_data(valid_weather_data)

    mock_connect.assert_called_once()
    mock_connection.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once()

    execute_args = mock_cursor.execute.call_args
    sql_query = execute_args.args[0]

    assert "ON CONFLICT" in sql_query
    assert "DO NOTHING" in sql_query

    assert execute_args.args[1] == valid_weather_data


@patch("src.load.psycopg.connect")
def test_load_weather_data_database_failure(
    mock_connect,
    valid_weather_data,
):
    mock_connect.side_effect = psycopg.OperationalError(
        "Simulated database connection failure"
    )

    with pytest.raises(
        RuntimeError,
        match="Database load failed"
    ):
        load_weather_data(valid_weather_data)