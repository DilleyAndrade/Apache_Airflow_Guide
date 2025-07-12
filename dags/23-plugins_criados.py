from airflow import DAG
from big_data_operator import BigDataOperator
#O arquivo está salvo na pasta /plugins

with DAG(
    '23-plugins',
    description='big_data dag',
    schedule=None,
    catchup=False
) as dag:

    big_data = BigDataOperator(
      task_id='big_data',
      path_to_csv_file = '/opt/airflow/data/Churn.csv', 
      path_to_save_file = '/opt/airflow/data/Churn_New.parquet', 
      file_type='parquet'
    )
    
    big_data 


