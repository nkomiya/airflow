from airflow.operators.python_operator import PythonOperator

from dependencies.util import OperatorDescriber


class XcomPush(OperatorDescriber):
    """Push XCom value to share a object with other tasks.
    """

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.push_scalar_value
        }

    def get_doc_md(self):
        return r"""\
            #### Description

            Push XCom value to share a object with other tasks.
            """

    def push_scalar_value(self):
        # returned value can be fetched in other tasks via xcom_pull
        return "value from XcomPush"
