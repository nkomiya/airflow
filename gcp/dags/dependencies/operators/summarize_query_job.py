import logging
import pytz

from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from google.cloud import bigquery

from dependencies.util import OperatorDescriber


class SummarizeQueryJob(OperatorDescriber):
    """Summarize BigQuery Query job result.

    Args:
        sql_task (str): ID of task where SQL is executed
        location (str): BigQuery region where SQL is executed
    """

    # XCom key to fetch BigQuery job ID
    KEY = "job_id"
    JST = pytz.timezone("Asia/Tokyo")
    DT_FMT = "%Y-%m-%d %H:%M:%S (JST)"

    def __init__(self, sql_task, location):
        self.sql_task = sql_task
        self.location = location

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.summarize,
            "provide_context": True,
        }

    def get_doc_md(self):
        return """\
            #### Description

            Summarize BigQuery Query job result.
            """

    def summarize(self, ti, **_):
        job_id = ti.xcom_pull(task_ids=self.sql_task, key=self.KEY)
        client = bigquery.Client(project=Variable.get("bq_project"))
        job = client.get_job(job_id, location=self.location)

        # Output logs about query job information
        logging.info("job state: %s", job.state)
        logging.info("started: %s", job.started.astimezone(self.JST).strftime(self.DT_FMT))
        logging.info("ended: %s", job.ended.astimezone(self.JST).strftime(self.DT_FMT))
        logging.info("bytes proccessed: %dB", job.total_bytes_processed)
