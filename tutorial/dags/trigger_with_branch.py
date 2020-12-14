from copy import deepcopy
from datetime import timedelta
from pathlib import Path

from airflow import DAG

from dependencies.operators import BranchByKey, StateControllable, TriggerConfigurable
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsTriggerWithBranch


DAG_ID = Path(__file__).stem
DESCRIPTION = 'A sample DAG includes a trigger configuration with workflow branching.'
DOC_MD = f"""\
#### DAG description

{DESCRIPTION}
"""

default_args = deepcopy(DEFAULT_ARGS)
default_args["retries"] = 0

with DAG(DAG_ID,
         default_args=default_args,
         description=DESCRIPTION,
         schedule_interval=timedelta(days=1)) as dag:
    # set dag description
    dag.doc_md = __doc__

    # build tasks
    task_a = IdsTriggerWithBranch.TASK_A
    task_b = IdsTriggerWithBranch.TASK_B
    t1 = BranchByKey().build(IdsTriggerWithBranch.BRANCH_OP)
    t2 = StateControllable(task_a.id).build(task_a)
    t3 = StateControllable(task_b.id).build(task_b)
    t4 = TriggerConfigurable().build(IdsTriggerWithBranch.TRIGGER_CONFIGURED)

    # task dependency
    t1 >> [t2, t3] >> t4
