from enum import Enum


class BaseTaskId(Enum):
    """Base Enum for manage task ids in a DAG"""

    @property
    def id(self):
        """str: task ID"""
        return self.name.lower()
