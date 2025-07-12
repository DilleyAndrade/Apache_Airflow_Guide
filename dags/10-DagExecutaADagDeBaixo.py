from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    '10-call_dag',
    description='Dag run dag',
    schedule=None,
    start_date=datetime(2025, 6, 30),
    catchup=False
) as dag:

    task1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    task2 = TriggerDagRunOperator(task_id='tsk2', trigger_dag_id='11-called_dag') #ID DA DAG QUE DESEJO CHAMAR
    
    task1 >> task2


