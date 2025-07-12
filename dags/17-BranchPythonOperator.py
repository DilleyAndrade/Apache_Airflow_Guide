from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
import random

def gera_numero_aleatorio(): #FUNÇÃO PARA GERAR UM NÚMERO ELEATÓRIO, PARA SERVIR DE VALIDADOR
  num = random.randint(1, 100)
  print(f'The random number is: {num}')
  return num

def avalia_numero_aleatorio(**context): #**context os argumentos que vamos precisar adicionar
  number = context['task_instance'].xcom_pull(task_ids='gera_numero_aleatorio_task') #vai pegar o valor gerado na função acima 
  if number % 2 == 0 :
    return 'par_task' #Se for o valor da função acima for par vai chamar a task "PAR_TASK"
  else:
    return 'impar_task' #Se for o valor da função acima impar par vai chamar a task "IMPAR_TASK"


with DAG(
  '17-branch_python_operator',
  description='Branch demo',
  schedule=None,
  catchup=False
) as dag:

  branch_task = BranchPythonOperator(
    task_id='branch_task', 
    python_callable=avalia_numero_aleatorio,
    #provide_context=True Não é mais necessária, nas novas versões do airflow o provider é adicionado automaticamente 
  )
  
  gera_numero_aleatorio_task = PythonOperator( 
    task_id = 'gera_numero_aleatorio_task', 
    python_callable = gera_numero_aleatorio
  )
  
  par_task = BashOperator(task_id='par_task', bash_command='echo "Número Par"') 
  impar_task = BashOperator(task_id='impar_task', bash_command='echo "Número Ímpar"')

gera_numero_aleatorio_task >> branch_task
branch_task >> par_task
branch_task >> impar_task