from datetime import timedelta

from airflow import DAG

from dependencies.operators import PrintDate, Sleep, Templated
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsQuickStart


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
    t1 = PrintDate().build(IdsQuickStart.PRINT_DATE)
    t2 = Sleep().build(IdsQuickStart.SLEEP)
    t3 = Templated().build(IdsQuickStart.TEMPLATED)

    # task dependency
    [t1, t2] >> t3
