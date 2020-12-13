import logging

from airflow.operators.python_operator import PythonOperator

from dependencies.util import OperatorDescriber


class XcomPushKv(OperatorDescriber):
    """Push XCom value to multiple objects.
    """

    KEYS = set(["key_1", "key_2"])

    def get_operator_class(self):
        return PythonOperator

    def get_operator_args(self):
        return {
            "python_callable": self.push_multi_values,
            "provide_context": True,
        }

    def get_doc_md(self):
        return r"""\
            #### Description

            Push XCom value to multiple objects.
            """

    def push_multi_values(self, ti, **_):
        for k in sorted(self.KEYS):
            v = k.replace("key", "val")
            logging.info("Push key-value: (%s, %s)", k, v)

            # key-value pair can be pushed via ti.xcom_push
            ti.xcom_push(key=k, value=v)
