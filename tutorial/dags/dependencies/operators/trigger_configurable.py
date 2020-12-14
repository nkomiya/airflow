import logging

from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

from dependencies.util import OperatorDescriber


class TriggerConfigurable(OperatorDescriber):
    """Build PythonOperator whose trigger is configurable via Airflow variable.

    Task trigger rule is obtained from Airflow variable `trigger_rule`.
    """

    TRIGGER_KEY = "trigger_rule"

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        rule = Variable.get(TriggerConfigurable.TRIGGER_KEY, default_var="").upper()
        if not hasattr(TriggerRule, rule):
            raise ValueError(f"Trigger rule {rule} is not defined in Airflow")

        return {
            "python_callable": self.run,
            "trigger_rule": getattr(TriggerRule, rule)
        }

    def get_doc_md(self):
        return """\
            #### Task documentation

            Run trigger configured task. The trigger rule is obtained from
            Airflow variable `trigger_rule`.
            """

    def run(self):
        """Run task.
        """
        logging.info("Task triggered")
