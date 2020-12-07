FROM apache/airflow:1.10.12

ADD start.sh /opt/airflow

EXPOSE 8080

CMD ["bash", "/opt/airflow/start.sh"]
