from enum import auto

from dependencies.util import BaseTaskId


class TaskId(BaseTaskId):

    CREATE_FILE = auto()
    UPLOAD_FILE = auto()
