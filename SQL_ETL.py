from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Shobana Thangavelu',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'mysql_etl_dag',  # DAG name
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2025, 7, 29),
    catchup=False,
)

run_etl = BashOperator(
    task_id='run_etl_mysql',
    bash_command='bash /home/emerg1/airflow/dags/wrapper.sh ',#give a space after the path
    dag=dag,
)

run_etl
