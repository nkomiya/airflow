from copy import deepcopy
from datetime import timedelta
from pathlib import Path

from airflow import DAG

from dependencies.operators import StateControllable, TriggerConfigurable
from dependencies.util import DEFAULT_ARGS
from dependencies.task_id import IdsTrigger


DAG_ID = Path(__file__).stem
DESCRIPTION = 'A sample DAG includes a trigger configured task.'
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
    t1 = StateControllable("task_a").build(IdsTrigger.TASK_A)
    t2 = StateControllable("task_b").build(IdsTrigger.TASK_B)
    t3 = TriggerConfigurable().build(IdsTrigger.TRIGGER_CONFIGURED)

    # task dependencies
    [t1, t2] >> t3
