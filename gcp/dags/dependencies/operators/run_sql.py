from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from google.cloud.bigquery import CreateDisposition, WriteDisposition

from dependencies.util import OperatorDescriber


class RunSql(OperatorDescriber):
    """Run BigQuery SQL and output result into table.

    Args:
        template (str): Path to SQL template file
        table (str): Output table name
        location (str): GCP region where SQL is executed
    """

    def __init__(self, template, table, location):
        self.template = template
        self.table = table
        self.location = location

    def get_operator_class(self):
        return BigQueryOperator

    def get_operator_args(self):
        return {
            "sql": self.template,
            "destination_dataset_table": f"{{{{var.value.bq_project}}}}.{{{{var.value.bq_dataset}}}}.{self.table}",
            "create_disposition": CreateDisposition.CREATE_IF_NEEDED,
            "write_disposition": WriteDisposition.WRITE_TRUNCATE,
            "use_legacy_sql": False,
            "location": self.location,
            "labels": {
                "component": "airflow"
            }
        }

    def get_doc_md(self):
        return """\
            #### Description

            Create BigQuery table by SQL.
            Output table will be truncated.
            """
