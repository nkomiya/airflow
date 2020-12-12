from datetime import timedelta
import os

from airflow import DAG

from dependencies.operators import RunSql
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsBigqueryOperator

DAG_ID = os.path.basename(__file__).split('.')[0]

# SQL template
TEMPLATE = f"sql/{DAG_ID}.sql"

# Resources
TABLE = "bigquery_operator"

# Descriptions
DESCRIPTION = 'Create BigQuery table'
DOC_MD = f"""\
#### Description

Create BigQuery table by SQL

##### Output BigQuery table detail

- project: Specified via variable `bq_project`
- dataset: Specified via variable `bq_dataset`
- table: Fixed to `{TABLE}`
"""


with DAG(DAG_ID,
         default_args=DEFAULT_ARGS,
         description=DESCRIPTION,
         schedule_interval=timedelta(days=1)) as dag:
    dag.doc_md = DOC_MD

    # build tasks
    t = RunSql(TEMPLATE, TABLE).build(IdsBigqueryOperator.RUN_SQL)
