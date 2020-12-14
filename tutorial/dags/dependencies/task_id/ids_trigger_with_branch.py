from enum import auto

from dependencies.util import BaseTaskId


class IdsTriggerWithBranch(BaseTaskId):

    BRANCH_OP = auto()
    TASK_A = auto()
    TASK_B = auto()
    TRIGGER_CONFIGURED = auto()
