from datetime import timedelta
import os

from airflow import DAG

from dependencies.operators import RunSql, SummarizeQueryJob
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsBigqueryOperator

DAG_ID = os.path.basename(__file__).split('.')[0]

# SQL template
TEMPLATE = f"sql/{DAG_ID}.sql"

# Resources
TABLE = "bigquery_operator"
LOCATION = "us"

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
    t1 = RunSql(TEMPLATE, TABLE, LOCATION).build(IdsBigqueryOperator.RUN_SQL)
    t2 = SummarizeQueryJob(IdsBigqueryOperator.RUN_SQL.id, LOCATION).build(IdsBigqueryOperator.SUMMARIZE)

    t1 >> t2
