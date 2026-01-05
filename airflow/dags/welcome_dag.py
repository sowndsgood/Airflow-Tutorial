from datetime import datetime
import requests

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def welcome_message():
    print("Welcome to Airflow!")

def print_current_time():
    print("Current time is: {}".format(datetime.now()))

def print_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote = response.json().get("content")
        print("Random quote: {}".format(quote))
    else:
        print("Failed to retrieve quote")

default_args = {
    "start_date": days_ago(1)
}

dag = DAG(
    dag_id="welcome_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

welcome_message_task = PythonOperator(
    task_id="welcome_message",
    python_callable=welcome_message,
    dag=dag
)

print_current_time_task = PythonOperator(
    task_id="print_current_time",
    python_callable=print_current_time,
    dag=dag
)

print_random_quote_task = PythonOperator(
    task_id="print_random_quote",
    python_callable=print_random_quote,
    dag=dag
)

welcome_message_task >> print_current_time_task >> print_random_quote_task