from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    '7-trigger_rule_all_fail',
    description='Nossa quinta dag trigger',
    schedule=None,
    start_date=datetime(2025, 6, 30),
    catchup=False
) as dag:

    task1 = BashOperator(task_id='tsk1', bash_command='exit 1') #Vai fazer a task falhar
    task2 = BashOperator(task_id='tsk2', bash_command='exit 1')
    task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', trigger_rule='all_failed')

    [task1, task2] >> task3
