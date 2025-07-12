from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

def print_result(ti):
  task_instance = ti.xcom_pull(task_ids='query_data')
  print('Resultado da consulta: ')
  for row in task_instance:
    print(row)

with DAG(
  '21-providers',
  description='Banco de dados Dag',
  schedule=None,
  catchup=False
) as dag:
  
  create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres',
    sql='create table teste(id int);'
  )

  insert_data = PostgresOperator(
    task_id='insert_data',
    postgres_conn_id='postgres',
    sql='insert into teste values (1);'
  )

  query_data = PostgresOperator(
    task_id='query_data',
    postgres_conn_id='postgres',
    sql='select * from teste;',
    do_xcom_push=True  # Adicione isso
  )

  print_result_task = PythonOperator(
    task_id = 'print_result_task',
    python_callable=print_result
  )

  create_table >> insert_data >> query_data >> print_result_task