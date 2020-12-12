from configparser import ConfigParser
from datetime import timedelta
import os
from pathlib import Path

from airflow import DAG

from dependencies.operators import CreateFile, UploadFile
from dependencies.util import DEFAULT_ARGS
from dependencies import TaskId

DAG_ID = os.path.basename(__file__).split('.')[0]
DESCRIPTION = 'Rename GCS object'
DOC_MD = """\
#### Description

This DAG rename GCS object
"""

# GCP configuration
parser = ConfigParser()
parser.read(Path(__file__).parent.joinpath("config").joinpath(DAG_ID + ".conf"))
TEMPORARY_FILE = parser.get("src", "path", fallback="/opt/airflow/work/temp.txt")
BUCKET = parser.get("dst", "bucket", fallback="")
NAME = parser.get("dst", "name", fallback="")

with DAG(DAG_ID,
         default_args=DEFAULT_ARGS,
         description=DESCRIPTION,
         schedule_interval=timedelta(days=1)) as dag:
    dag.doc_md = DOC_MD

    # build tasks
    t1 = CreateFile(TEMPORARY_FILE).build(TaskId.CREATE_FILE)
    t2 = UploadFile(TEMPORARY_FILE, BUCKET, NAME).build(TaskId.UPLOAD_FILE)

    # configure dependencies
    t1 >> t2
