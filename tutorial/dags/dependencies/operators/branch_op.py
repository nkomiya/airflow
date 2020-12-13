from datetime import datetime

from airflow.operators.python_operator import BranchPythonOperator
import pytz

from dependencies.util import OperatorDescriber


class BranchOp(OperatorDescriber):
    """Branch workflow based on whether the run date is weekdays or not.

    Args:
        on_weekdays (str): ID of task which is executed on weekdays
        on_weekends (str): ID of task which is executed on weekends
    """
    DT_FMT = "%Y-%m-%d"
    JST = pytz.timezone("Asia/Tokyo")

    def __init__(self, on_weekdays, on_weekends):
        self.on_weekdays = on_weekdays
        self.on_weekends = on_weekends

    def get_operator_class(self):
        return BranchPythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.branch_fn,
            "provide_context": True,
        }

    def get_doc_md(self):
        return """\
            ####Task documentation

            Designate subsequent task based on whether the run date is weekdays or not.
            """

    def branch_fn(self, ds, **_):
        run_date = pytz.utc.localize(datetime.strptime(ds, self.DT_FMT)).astimezone(self.JST)
        if run_date.weekday() < 5:
            return self.on_weekdays
        else:
            return self.on_weekends
