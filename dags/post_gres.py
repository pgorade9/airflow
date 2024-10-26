from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

dag = DAG("post_gres_dag")

create_table = PostgresOperator(task_id="create_table", postgres_conn_id="pg_db", sql="""CREATE TABLE IF NOT 
EXISTS my_books( id SERIAL PRIMARY KEY, title TEXT NOT NULL, pages INT);""", dag=dag)

fetch_books = PostgresOperator(task_id="make_entry", postgres_conn_id="pg_db", sql="""INSERT INTO my_books 
VALUES ( 1, 'REST API Fundamentals', 100);""", dag=dag)

create_table >> fetch_books
