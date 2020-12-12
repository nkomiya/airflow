from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator

from dependencies.util import OperatorDescriber


class UploadFile(OperatorDescriber):
    """Upload file to Google Cloud Storage.

    Args:
        local_file_path (str): local file path to be uploaded
        name (str): Output GCS object name
    """

    def __init__(self, local_file_path, name):
        self.local_file_path = local_file_path
        self.name = name

    def get_operator_class(self):
        return FileToGoogleCloudStorageOperator

    def get_operator_args(self):
        return {
            "src": self.local_file_path,
            "bucket": "{{ var.value.gcs_bucket }}",
            "dst": self.name,
        }

    def get_doc_md(self):
        return """\
            #### Description

            Upload file to google cloud storage.
            Destination bucket is determined by variable `gcs_bucket`.
            """
