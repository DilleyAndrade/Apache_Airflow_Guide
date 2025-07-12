from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
  '15-pools',
  description='Pool demo',
  schedule=None,
  catchup=False
) as dag:
  task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', pool='meupool') #Definido na interface gráfica do airflow com o valor de 1 slot
  task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', pool='meupool', priority_weight=5)
  task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', pool='meupool')
  task4 = BashOperator(task_id='tsk4', bash_command='sleep 5', pool='meupool', priority_weight=10)
  

  #POOL FAZ UM GERENCIAMENTO DE RECURSO NA EXECUÇÃO DAS DAGS, PARA DEFINIR QUEM DEVE GASTAR MAIS PARA SER EXECUTADA PRIMEIRO