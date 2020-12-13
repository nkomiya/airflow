from datetime import timedelta
from pathlib import Path

from airflow import DAG

from dependencies.operators import XcomPullKv, XcomPushKv
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsXcom


DAG_ID = Path(__file__).stem
DESCRIPTION = 'A sample DAG using xcom in PythonOperator'
DOC_MD = f"""\
#### DAG description

{DESCRIPTION}
"""

with DAG(DAG_ID,
         default_args=DEFAULT_ARGS,
         description=DESCRIPTION,
         schedule_interval=timedelta(days=1)) as dag:
    # set dag description
    dag.doc_md = __doc__

    # pass scalar value
    t1 = XcomPushKv().build(IdsXcom.XCOM_PUSH)
    t2 = XcomPullKv(IdsXcom.XCOM_PUSH.id, XcomPushKv.KEYS).build(IdsXcom.XCOM_PULL)

    # task dependency
    t1 >> t2
