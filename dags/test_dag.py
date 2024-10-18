from airflow import DAG
from airflow.operators.python import PythonOperator
from pprint import pprint

dag = DAG("test_dag")


def print_context(arg1, **kwargs):
    print(arg1)
    pprint(kwargs)
    return f"{arg1} function gets printed in the logs"


run_this = PythonOperator(task_id="print_this_context", python_callable=print_context, dag=dag,
                          op_args=['this'],
                          op_kwargs={'kwarg1': 'value1', 'kwarg2': 'value2'})

run_that = PythonOperator(task_id="print_that_context", python_callable=print_context, dag=dag,
                          op_args=['that'],
                          op_kwargs={'kwarg3': 'value3', 'kwarg4': 'value4'})

run_this >> run_that
