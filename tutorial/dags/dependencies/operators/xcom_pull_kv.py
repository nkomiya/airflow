import logging

from airflow.operators.python_operator import PythonOperator

from dependencies.util import OperatorDescriber


class XcomPullKv(OperatorDescriber):
    """Pull XCom values and output it to log.

    Args:
        task_id (str): ID of task where value is pulled from
        keys (Iterable[str]): XCom keys for pulling values
    """

    def __init__(self, task_id, keys):
        self.task_id = task_id
        self.keys = keys

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

            Pull XCom values and output it to log
            """

    def pull_scalar_value(self, ti, **_):
        t = self.task_id
        logging.info("Pull value from task %s", t)
        for k in self.keys:
            # Given XCom value for key `k` can be obtained by ti.xcom_pull
            v = ti.xcom_pull(task_ids=t, key=k)

            logging.info("  (key, value) = (%s, %s)", k, v)
