from datetime import timedelta

from airflow.utils.dates import days_ago

from ._base_task_id import BaseTaskId
from ._operator_describer import OperatorDescriber

__all__ = ['DEFAULT_ARGS', 'BaseTaskId', 'OperatorDescriber']

DEFAULT_ARGS = {
    'owner': 'example',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': None,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
