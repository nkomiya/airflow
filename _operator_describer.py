from abc import ABCMeta, abstractmethod
from textwrap import dedent

from airflow.operators import BaseOperator


class OperatorDescriber(metaclass=ABCMeta):
    """Abstract class to simplify describing airflow operator

    Example:
        .. code-block:: python

            from airflow.operators.bash_operator import BashOperator

            class SampleOperator(OperatorDescriber):

                def get_operator_class(self):
                    # Specify airflow operator class
                    return BashOperator

                def get_operator_args(self):
                    # Specify arguments which is passed to airflow operator class
                    return {
                        "bash_command": "echo hello"
                    }

                def get_doc_md(self):
                    # Specify description on airflow task in markdown format.
                    # Indentation will be omitted.
                    return '''\\
                        ### Description

                        This task output string 'hello'
                        '''
    """

    @abstractmethod
    def get_operator_class(self):
        """Get Airflow operator class

        Returns:
            type: subclass of airflow BaseOperator
        """
        pass

    @abstractmethod
    def get_operator_args(self):
        """Get arguments for airflow operator, but except task_id

        Returns:
            dict: arguments list
        """
        pass

    @abstractmethod
    def get_doc_md(self):
        """Get description of task in markdown format

        Returns:
            str: description
        """
        pass

    def build(self, task_id):
        """build airflow operator

        Args:
            task_id (BaseTaskId): enum value for ID of task in dag
        """
        # get parameters for airflow operater
        clz = self.get_operator_class()
        op_kwds = self.get_operator_args()
        doc_md = self.get_doc_md()

        # type assertion
        self._validate(clz, op_kwds, doc_md)

        # build operator
        op = clz(task_id=task_id.id, **op_kwds)
        op.doc_md = dedent(doc_md)
        return op

    def _validate(self, clz, op_kwds, doc_md):
        """Validate subclass implementation
        """
        if not (type(clz) == type and issubclass(clz, BaseOperator)):
            return TypeError(f"Method get_operator_class should return subclass of BaseOperator, but got {type(clz)}")

        if type(op_kwds) != dict:
            raise TypeError(f"Method get_operator_args should return dict, but got {type(op_kwds)}")

        if type(doc_md) != str:
            raise TypeError(f"Method get_doc_md should return string, but got {type(doc_md)}")
