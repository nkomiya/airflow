from airflow.operators.bash_operator import BashOperator

from dependencies.util import OperatorDescriber


class PrintDate(OperatorDescriber):

    def get_operator_class(self):
        return BashOperator

    def get_operator_args(self):
        return {
            "bash_command": "date"
        }

    def get_doc_md(self):
        return """\
            ####Task documentation

            You can document your task using the attributes `doc_md` (markdown),
            `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
            rendered in the UI's Task Instance Details page.

            ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
            """
