import requests


API_URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 39.9612,
    "longitude": -82.9988,
    "current": (
        "temperature_2m,"
        "relative_humidity_2m,"
        "wind_speed_10m,"
        "weather_code"
    ),
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph",
}


def extract_weather_data():
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    response.raise_for_status()

    weather_data = response.json()

    return weather_data


if __name__ == "__main__":
    data = extract_weather_data()
    print(data)