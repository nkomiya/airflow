from datetime import timedelta
from pathlib import Path

from airflow import DAG

from dependencies.operators import BranchOp, OnWeekDays, OnWeekEnds
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsBranching


DAG_ID = Path(__file__).stem
DESCRIPTION = 'A sample DAG includes branching'
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

    # build tasks
    weekdays = IdsBranching.ON_WEEKDAYS
    weekends = IdsBranching.ON_WEEKENDS
    t1 = BranchOp(weekdays.id, weekends.id).build(IdsBranching.BRANCH_OP)
    t2 = OnWeekDays().build(weekdays)
    t3 = OnWeekEnds().build(weekends)

    # task dependency
    t1 >> [t2, t3]
