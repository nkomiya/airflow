import logging

from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

from dependencies.util import OperatorDescriber


class StateControllable(OperatorDescriber):
    """Build PythonOperator whose state is controlled by Airflow variable.

    The task results into failure if the value for key `variable_key` is not ok.

    Args:
        variable_key (str): Airflow variable key which designates task state
    """

    def __init__(self, variable_key):
        self.variable_key = variable_key

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.run
        }

    def get_doc_md(self):
        return f"""\
            #### Task documentation

            Run task whose state is controlled via Airflow variable `{self.variable_key}`.
            The task results in failure when the value of `{self.variable_key}` is not ok.
            """

    def run(self):
        """Run task.

        Raises:
            RuntimeError: when the value for key `variable_key` is not ok.
        """
        var = Variable.get(self.variable_key, default_var="NOT FOUND")
        if var == "ok":
            logging.info("Task success")
        else:
            raise RuntimeError("Task failed, value for {}: {}".format(self.variable_key, var))
