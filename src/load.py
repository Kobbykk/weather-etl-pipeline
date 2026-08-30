import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


def load_weather_data(weather_data):
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    insert_query = """
        INSERT INTO weather_observations (
            city,
            latitude,
            longitude,
            temperature_f,
            humidity_percent,
            wind_speed_mph,
            weather_code,
            observation_time,
            ingested_at
        )
        VALUES (
            %(city)s,
            %(latitude)s,
            %(longitude)s,
            %(temperature_f)s,
            %(humidity_percent)s,
            %(wind_speed_mph)s,
            %(weather_code)s,
            %(observation_time)s,
            %(ingested_at)s
        )
        ON CONFLICT (city, observation_time)
        DO NOTHING;
    """

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(insert_query, weather_data)

    connection.close()