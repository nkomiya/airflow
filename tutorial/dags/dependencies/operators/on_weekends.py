from airflow.operators.bash_operator import BashOperator

from dependencies.util import OperatorDescriber


class OnWeekEnds(OperatorDescriber):

    def get_operator_class(self):
        return BashOperator

    def get_operator_args(self):
        return {
            "bash_command": "echo This is task for weekends"
        }

    def get_doc_md(self):
        return """\
            #### Task documentation

            Task to be executed on weekends.
            """
