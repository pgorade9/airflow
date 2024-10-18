from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

dag = DAG("post_gres_dag")

create_table = PostgresOperator(task_id="create_table", postgres_conn_id="pg_db",sql="""CREATE TABLE IF NOT 
EXISTS my_books( id SERIAL PRIMARY KEY, title TEXT NOT NULL, pages INT);""",dag=dag)
