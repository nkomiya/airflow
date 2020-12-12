from datetime import timedelta
import os

from airflow import DAG

from dependencies.operators import CreateFile, UploadFile
from dependencies.util import DEFAULT_ARGS
from dependencies import TaskId

DAG_ID = os.path.basename(__file__).split('.')[0]

# Resources
TEMPORARY_FILE = "/opt/airflow/work/temp.txt"
NAME = f"{DAG_ID}/result.txt"

# Descriptions
DESCRIPTION = 'Upload file to GCS'
DOC_MD = f"""\
#### Description

Upload a file to GCS.

##### Output GCS object detail

- bucket: Specified via variable `gcs_bucket`
- name: Fixed to `{NAME}`
"""

with DAG(DAG_ID,
         default_args=DEFAULT_ARGS,
         description=DESCRIPTION,
         schedule_interval=timedelta(days=1)) as dag:
    dag.doc_md = DOC_MD

    # build tasks
    t1 = CreateFile(TEMPORARY_FILE).build(TaskId.CREATE_FILE)
    t2 = UploadFile(TEMPORARY_FILE, NAME).build(TaskId.UPLOAD_FILE)

    # configure dependencies
    t1 >> t2
