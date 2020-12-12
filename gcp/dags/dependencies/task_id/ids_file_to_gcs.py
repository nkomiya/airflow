from enum import auto

from dependencies.util import BaseTaskId


class IdsFileToGcs(BaseTaskId):

    CREATE_FILE = auto()
    UPLOAD_FILE = auto()
