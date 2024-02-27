from datetime import datetime, timedelta
from email.policy import default
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PythonOperator

default_args={
    'owner': 'Enzo_CoderHouse',
    'retries':5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='dag_tp_cuatro',
    description= 'Dag para el trabajo práctico 4 de Data Engineering',
    start_date=datetime(2024,2,25),
    schedule_interval='0 3 * * *'
    ) as dag:


    task = PythonOperator(
        task_id='ingesta_e_insercion_datos',
       python_callable = entregatresde,
       dag = dag,
    )
    
task