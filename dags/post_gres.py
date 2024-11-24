from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

# This DAG is a demo of using PostgresOperator
dag = DAG("post_gres_dag")

# This task will create table IF NOT present
create_table = PostgresOperator(task_id="create_table", postgres_conn_id="pg_db", sql="""CREATE TABLE IF NOT 
EXISTS my_books( id SERIAL PRIMARY KEY, title TEXT NOT NULL, pages INT);""", dag=dag)

# This task will run only one time. Next time same entry won't be allowed due primary key validation by postgres
fetch_books = PostgresOperator(task_id="make_entry", postgres_conn_id="pg_db", sql="""INSERT INTO my_books 
VALUES ( 3, 'Efficient Angular', 200);""", dag=dag)

create_table >> fetch_books
