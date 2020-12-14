from airflow.models import Variable
from airflow.operators.python_operator import BranchPythonOperator

from dependencies.util import OperatorDescriber


class BranchByKey(OperatorDescriber):
    """Branch workflow.

    Subsequent task is determined from Airflow variable named `branch_key`
    """
    BRANCH_KEY = "branch_key"

    def get_operator_class(self):
        return BranchPythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.branch_fn,
        }

    def get_doc_md(self):
        return """\
            #### Task documentation

            Branch workflow.

            Subsequent task is determined from Airflow variable named `branch_key`
            """

    def branch_fn(self):
        return Variable.get(BranchByKey.BRANCH_KEY, default_var="")
