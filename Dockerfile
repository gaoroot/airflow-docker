FROM apache/airflow:2.9.1-python3.11
USER root
RUN apt-get update && apt-get install -y mc
USER ${AIRFLOW_UID}
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir sqlalchemy==2.0.2
RUN pip install -r /requirements.txt