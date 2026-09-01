from extract import extract_weather_data
from transform import transform_weather_data
from validate import validate_weather_data
from load import load_weather_data


raw_data = extract_weather_data()

clean_data = transform_weather_data(raw_data)

validate_weather_data(clean_data)

load_weather_data(clean_data)

print("Weather data loaded successfully.")