import logging
import os

from airflow.operators.python_operator import PythonOperator

from dependencies.util import OperatorDescriber


class CreateFile(OperatorDescriber):
    """Python operator which outputs run date to file.

    Args:
        file_path (str): Output file path
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.create_file,
            "provide_context": True,
            "op_kwargs": {
                "file_path": self.file_path
            }
        }

    def get_doc_md(self):
        return """\
            #### Description

            Output run date to a file.
            File path is designated by the attribute `op_kwargs.file_path`.
            """

    def create_file(self, ds, file_path, **_):
        """Python callable executed by PythonOperator

        Args:
            ds (str): run date
        """
        dirname = os.path.dirname(file_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(file_path, "w") as f_obj:
            f_obj.write(ds)

        logging.info(f"File created: {os.path.abspath(file_path)}")
