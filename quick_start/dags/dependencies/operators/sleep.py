from airflow.operators.bash_operator import BashOperator

from dependencies.util import OperatorDescriber


class Sleep(OperatorDescriber):

    @classmethod
    def get_operator_class(cls):
        return BashOperator

    @classmethod
    def get_operator_args(cls):
        return {
            "bash_command": "sleep 1"
        }

    @classmethod
    def get_doc_md(cls):
        return """\
            #### Task description

            sleep 1 second
            """
