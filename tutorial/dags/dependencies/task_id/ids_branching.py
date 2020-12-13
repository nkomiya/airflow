from enum import auto

from dependencies.util import BaseTaskId


class IdsBranching(BaseTaskId):

    BRANCH_OP = auto()
    ON_WEEKDAYS = auto()
    ON_WEEKENDS = auto()
