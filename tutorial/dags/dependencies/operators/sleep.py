from airflow.operators.bash_operator import BashOperator

from dependencies.util import OperatorDescriber


class Sleep(OperatorDescriber):

    def get_operator_class(self):
        return BashOperator

    def get_operator_args(self):
        return {
            "bash_command": "sleep 1"
        }

    def get_doc_md(self):
        return """\
            #### Task description

            sleep 1 second
            """
