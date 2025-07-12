from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
  '13-empty_operator',
  description='Task Empty demo',
  schedule=None,
  catchup=False
) as dag:
  task1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
  task2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
  task3 = BashOperator(task_id='tsk3', bash_command='sleep 5')
  task_dummy = EmptyOperator(task_id='tsk4') #Operador vazio, para fazer a ligação entreas tasks
  task5 = BashOperator(task_id='tsk5', bash_command='sleep 5')
  task6 = BashOperator(task_id='tsk6', bash_command='sleep 5')

[task1, task2, task3] >> task_dummy
task_dummy >> [task5, task6]