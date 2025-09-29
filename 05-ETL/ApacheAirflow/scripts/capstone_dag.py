# Import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Chain helper
from airflow.sdk import chain
# Operators; you need this to write tasks!
from airflow.providers.standard.operators.bash import BashOperator
# This makes scheduling easy
import pendulum

# *** Default Arguments on the DAG
default_args = {
    'owner': 'Your name',
    'start_date': pendulum.today(),
    'email': ['bert@catsburg.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# *** DAG definition
dag = DAG(
    dag_id='capstone_DAG',
    default_args=default_args,
    description='Capstone DAG',
    schedule=timedelta(days=1),
    tags=['capstone'],
)

# *** Data
access_log_file = "./access.log"

# *** Define the Tasks
task_extract_data = BashOperator(
    task_id='extract_data',
    bash_command="cat /opt/airflow/dags/data/accesslog.txt | awk '{print $1}' > /opt/airflow/dags/data/extracted_data.txt",
    dag=dag,
)

task_transform_data = BashOperator(
    task_id='transform_data',
    bash_command='cat /opt/airflow/dags/data/extracted_data.txt | grep -v "198.46.149.143" > /opt/airflow/dags/data/transformed_data.txt',
)
#  tar tvf weblog.tar

task_load_data = BashOperator(
    task_id='load_data',
    bash_command='tar cvf /opt/airflow/dags/data/weblog.tar /opt/airflow/dags/data/transformed_data.txt',
)


chain(task_extract_data, task_transform_data, task_load_data)
