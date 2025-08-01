from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    '2-paralelismo',
    description='Dag paralelismo',
    schedule=None,
    start_date=datetime(2025, 6, 30),
    catchup=False
) as dag:

    task1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    task2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
    task3 = BashOperator(task_id='tsk3', bash_command='sleep 5')

    task1 >> [task2, task3]
