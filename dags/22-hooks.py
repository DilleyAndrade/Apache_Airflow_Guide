from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

def create_table():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    pg_hook.run('create table if not exists teste2 (id int);', autocommit=True)

def insert_data():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    pg_hook.run('insert into teste2 values(1);', autocommit=True)

def select_data(**kwargs):
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    records = pg_hook.get_records('select * from teste2;')
    return records  # moderno: usa XCom via return

def print_data(**kwargs):
    ti = kwargs["ti"]
    result = ti.xcom_pull(task_ids="select_data_task")
    print("Dados da tabela:")
    for row in result:
        print(row)

with DAG(
    dag_id='22-hook',
    description='hook Dag',
    schedule=None,
    start_date=datetime(2025, 7, 12),
    catchup=False
) as dag:

    create_table_task = PythonOperator(
        task_id='create_table_task',
        python_callable=create_table
    )

    insert_data_task = PythonOperator(
        task_id='insert_data_task',
        python_callable=insert_data
    )

    select_data_task = PythonOperator(
        task_id='select_data_task',
        python_callable=select_data
    )

    print_data_task = PythonOperator(
        task_id='print_data_task',
        python_callable=print_data
    )

    create_table_task >> insert_data_task >> select_data_task >> print_data_task
