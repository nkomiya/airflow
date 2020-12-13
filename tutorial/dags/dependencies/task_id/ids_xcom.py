from enum import auto

from dependencies.util import BaseTaskId


class IdsXcom(BaseTaskId):

    XCOM_PUSH = auto()
    XCOM_PULL = auto()
