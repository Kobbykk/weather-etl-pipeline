from datetime import timedelta

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="weather_etl_pipeline",
    schedule="*/30 * * * *",
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=2),
    },
    tags=["weather", "etl", "portfolio"],
) as dag:

    run_weather_etl = BashOperator(
        task_id="run_weather_etl",
        bash_command="python /opt/airflow/src/main.py",
    )