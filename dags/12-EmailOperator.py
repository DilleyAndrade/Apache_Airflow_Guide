from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

default_args = {
  'depends_on_past': False,
  'start_date': datetime(2025,7,1),
  'email': ['dilleyandrade@gmail.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(seconds=10)
}

with DAG(
  '12-sending_email',
  description='Email airflow',
  default_args = default_args,
  schedule=None,
  catchup=False,
  tags=['email', 'airflow', 'teste']
) as dag:

  task1 = BashOperator(task_id='tsk1', bash_command='sleep 1')
  task2 = BashOperator(task_id='tsk2', bash_command='sleep 1')
  task3 = BashOperator(task_id='tsk3', bash_command='sleep 1')
  task4 = BashOperator(task_id='tsk4', bash_command='exit 1')
  task5 = BashOperator(task_id='tsk5', bash_command='sleep 1', trigger_rule='one_failed')
  task6 = BashOperator(task_id='tsk6', bash_command='sleep 1', trigger_rule='one_failed')

  send_email = EmailOperator(
      task_id='send_email',
      to='dilleyandrade@gmail.com',
      subject='DAG Falhou!',
      html_content='<h3>Uma task falhou na DAG <strong>email_test</strong></h3>',
      trigger_rule='one_failed',
      conn_id='gmail_smtp'
  )

  [task1, task2] >> task3 >> task4
  task4 >> [task5, task6, send_email]