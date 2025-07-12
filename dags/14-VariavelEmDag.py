from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

def print_variable(**context):
  my_var = Variable.get('myvar') #minhavar foidefinido dentro do airflow, tendo como valor uma string com o diretório de uma pasta
  print(f'O valor da minha variável é: {my_var}')

with DAG(
  '14-variable',
  description='Variables demo',
  schedule=None,
  catchup=False
) as dag:
  task1 = PythonOperator(task_id='tsk1', python_callable=print_variable)

  task1
  