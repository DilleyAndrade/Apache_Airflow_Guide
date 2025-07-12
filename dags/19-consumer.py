from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator
import pandas as pd

mydataset = Dataset('/opt/airflow/data/Churn_New.csv')

def my_file():
  dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
  dataset.to_csv('/opt/airflow/data/Churn_New.csv', sep=';')

with DAG(
  '19-consumer',
  description='consumer dag',
  schedule=[mydataset],
  catchup=False
) as dag:
  task1 = PythonOperator(task_id='tsk1', python_callable=my_file)


task1