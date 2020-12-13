from airflow.operators.bash_operator import BashOperator

from dependencies.util import OperatorDescriber


class Templated(OperatorDescriber):

    CMD_TEMPLATE = """
    {%- for i in range(2) -%}
      echo "{{ i }}th execution"
      echo "  Today: {{ ds }}"
      echo "  Tomorrow: {{ macros.ds_add(ds, 1) }}"
      echo "  Parameter: {{ params.var1 }}"
    {% endfor -%}
    """

    def get_operator_class(self):
        return BashOperator

    def get_operator_args(self):
        return {
            "bash_command": self.CMD_TEMPLATE,
            "params": {
                "var1": "parameter"
            }
        }

    def get_doc_md(self):
        return """\
            #### Task description

            Bash operator using jinja template & parameter
            """
