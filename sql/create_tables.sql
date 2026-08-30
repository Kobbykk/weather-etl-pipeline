CREATE TABLE IF NOT EXISTS weather_observations (
    id BIGSERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    temperature_f DOUBLE PRECISION NOT NULL,
    humidity_percent INTEGER NOT NULL,
    wind_speed_mph DOUBLE PRECISION NOT NULL,
    weather_code INTEGER NOT NULL,
    observation_time TIMESTAMPTZ NOT NULL,
    ingested_at TIMESTAMPTZ NOT NULL,
    CONSTRAINT unique_city_observation
        UNIQUE (city, observation_time)
);