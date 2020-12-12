from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator

from dependencies.util import OperatorDescriber


class UploadFile(OperatorDescriber):
    """Upload file to Google Cloud Storage

    Args:
        local_file_path (str): local file path to be uploaded
        bucket (str): Output GCS bucket name
        name (str): Output GCS object name
    """

    def __init__(self, local_file_path, bucket, name):
        self.local_file_path = local_file_path
        self.bucket = bucket
        self.name = name

    def get_operator_class(self):
        return FileToGoogleCloudStorageOperator

    def get_operator_args(self):
        return {
            "src": self.local_file_path,
            "bucket": self.bucket,
            "dst": self.name,
        }

    def get_doc_md(self):
        return """\
            #### Description

            Upload file to google cloud storage
            """
