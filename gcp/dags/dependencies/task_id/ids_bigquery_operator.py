from enum import auto

from dependencies.util import BaseTaskId


class IdsBigqueryOperator(BaseTaskId):

    RUN_SQL = auto()
    SUMMARIZE = auto()
