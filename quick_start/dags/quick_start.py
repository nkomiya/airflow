from datetime import timedelta

from airflow import DAG

from dependencies.operators import PrintDate, Sleep, Templated
from dependencies.util import DEFAULT_ARGS
from dependencies import TaskId


DAG_ID = 'quick_start'
DESCRIPTION = 'A simple DAG'
DOC_MD = """\
#### DAG description

A simple DAG for quick start
"""

with DAG(DAG_ID,
         default_args=DEFAULT_ARGS,
         description=DESCRIPTION,
         schedule_interval=timedelta(days=1)) as dag:
    # set dag description
    dag.doc_md = __doc__

    # whole tasks
    t1 = PrintDate().build(TaskId.PRINT_DATE)
    t2 = Sleep().build(TaskId.SLEEP)
    t3 = Templated().build(TaskId.TEMPLATED)

    # task dependency
    [t1, t2] >> t3
