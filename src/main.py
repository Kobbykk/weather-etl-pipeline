from extract import extract_weather_data
from transform import transform_weather_data
from validate import validate_weather_data
from load import load_weather_data
from logger import get_logger


logger = get_logger()


def main():
    logger.info("Starting weather pipeline")

    try:
        raw_data = extract_weather_data()
        logger.info("Weather data extracted successfully")

        clean_data = transform_weather_data(raw_data)
        logger.info("Weather data transformed successfully")

      

        validate_weather_data(clean_data)
        logger.info("Weather data validated successfully")

        load_weather_data(clean_data)
        logger.info("Weather data loaded successfully")

        logger.info("Weather pipeline completed successfully")

    except Exception:
        logger.exception("Weather pipeline failed")
        raise


if __name__ == "__main__":
    main()