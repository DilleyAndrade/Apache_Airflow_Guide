from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

with DAG(
    '9-task_group',
    description='Agrupamento com task group',
    schedule=None,
    start_date=datetime(2025, 6, 30),
    catchup=False
) as dag:

    task1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    task2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
    task3 = BashOperator(task_id='tsk3', bash_command='sleep 5')
    task4 = BashOperator(task_id='tsk4', bash_command='sleep 5')
    task5 = BashOperator(task_id='tsk5', bash_command='sleep 5')
    task6 = BashOperator(task_id='tsk6', bash_command='sleep 5')

    with TaskGroup('tsk_group') as tsk_group:
        task7 = BashOperator(task_id='tsk7', bash_command='sleep 5',)
        task8 = BashOperator(task_id='tsk8', bash_command='sleep 5',)
        task9 = BashOperator(task_id='tsk9', bash_command='sleep 5', trigger_rule='one_failed')

    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5 >> task6
    task6 >> tsk_group
    
