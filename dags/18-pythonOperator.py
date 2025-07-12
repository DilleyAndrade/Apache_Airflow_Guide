from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import statistics as sts

def data_clean():
  df = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
  df.columns = ['Id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Salario', 'Saiu']
  mediana = sts.median(df['Salario'])
  df['Salario'].fillna(mediana, inplace=True) #Onde o salario for nulo vou adicionar uma mediana
  df['Genero'].fillna('Masculino', inplace=True)
  mediana = sts.median(df['Idade'])
  df.loc[(df['Idade'] < 0) | (df['Idade'] > 120), 'Idade'] = mediana #Calcular a mediana da idade
  df.drop_duplicates(subset='Id', keep='first', inplace=True)

  df.to_parquet('/opt/airflow/data/Churn_Clean.parquet', compression='snappy', index=False)
  
with DAG(
  '18-python_operator',
  description='Python operator demo',
  schedule=None,
  catchup=False
) as dag:
  task1 = PythonOperator(task_id='tsk1', python_callable=data_clean)

  task1