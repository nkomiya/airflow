import logging

from airflow.operators.python_operator import PythonOperator

from dependencies.util import OperatorDescriber


class XcomPull(OperatorDescriber):
    """Pull XCom value and output it to log.

    Args:
        task_id (str): ID of task where value is pulled from
    """

    def __init__(self, task_id):
        self.task_id = task_id

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.pull_scalar_value,
            "provide_context": True
        }

    def get_doc_md(self):
        return """\
            #### Description

            Pull XCom value and output it to log
            """

    def pull_scalar_value(self, ti, **_):
        t = self.task_id
        logging.info("Pull value from task %s: %s", t, ti.xcom_pull(task_ids=t))
