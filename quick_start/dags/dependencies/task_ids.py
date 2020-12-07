from enum import auto

from dependencies.util import BaseTaskId


class TaskId(BaseTaskId):

    PRINT_DATE = auto()
    SLEEP = auto()
    TEMPLATED = auto()
