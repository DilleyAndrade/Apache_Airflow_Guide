from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
import requests

def query_api():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    print(response.text)

with DAG(
   '20-http_sensor',
    description='Http sensor demo',
    schedule=None,
    catchup=False
) as dag:

    check_api = HttpSensor(
        task_id='check_api',
        http_conn_id='connection',  # Precisa existir no Airflow
        endpoint='api/v2/pokemon/ditto',
        poke_interval=5,
        timeout=20
    )

    process_data = PythonOperator(
        task_id='process_data',
        python_callable=query_api
    )

    check_api >> process_data