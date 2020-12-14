from enum import auto

from dependencies.util import BaseTaskId


class IdsTrigger(BaseTaskId):

    TASK_A = auto()
    TASK_B = auto()
    TRIGGER_CONFIGURED = auto()
