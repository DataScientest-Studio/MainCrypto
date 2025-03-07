from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 2,
    #'schedule_interval': None,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id="scoring_model_dag",
    default_args=default_args,
    description="Un DAG pour lancer le calcul du modèle",
    schedule_interval="@daily", #None,
    catchup=False,
    tags=['model', 'scoring'],

) as my_dag:

    train_model = BashOperator(
        task_id="evaluate_model",
        bash_command= " cd ../../app/scripts && python3 evaluate_model2.py --currency='BTC-USD' --asset='XXBTZUSD'",
        do_xcom_push=True,
        dag=my_dag
    )



