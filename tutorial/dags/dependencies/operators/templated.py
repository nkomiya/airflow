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

    @classmethod
    def get_operator_class(cls):
        return BashOperator

    @classmethod
    def get_operator_args(cls):
        return {
            "bash_command": cls.CMD_TEMPLATE,
            "params": {
                "var1": "parameter"
            }
        }

    @classmethod
    def get_doc_md(cls):
        return """\
            #### Task description

            Bash operator using jinja template & parameter
            """
