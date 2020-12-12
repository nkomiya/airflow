# gcp

<!-- TOC -->

- [gcp](#gcp)
    - [Usage](#usage)
        - [Setup docker container](#setup-docker-container)
            - [Start container](#start-container)
            - [Setup credential](#setup-credential)
                - [Copy key file](#copy-key-file)
            - [Configure Airflow variables](#configure-airflow-variables)
            - [Configure Airflow connections](#configure-airflow-connections)
    - [DAGs](#dags)
    - [Build API doc](#build-api-doc)

<!-- /TOC -->

## Usage

### Setup docker container

#### Start container

Activate Airflow web UI on [localhost](http://localhost:8080).

```bash
# start container
$ docker run -d --rm --name airflow -p 8080:8080 \
    --env GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/key.json \
    --volume $(git rev-parse --show-toplevel)/gcp/dags:/opt/airflow/dags \
    airflow

# set alias
$ alias airflow='docker exec airflow airflow'
```

> **NOTE**:
> Authentication to Google Cloud Platform APIs is accomplished using application default credential.
> For more information on authentication mechanisms in airflow, check [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection/gcp.html#authenticating-to-gcp).

#### Setup credential

Following operations assume accessing GCP project using an service account.
Before proceeding,

1. Create service account, and grant proper privileges to the account (see [below](#dags))
1. Download service account key file

##### Copy key file

Copy service account key file to docker container.

```bash
# GOOGLE_APPLICATION_CREDENTIALS=/path/to/key/file.json
$ docker cp ${GOOGLE_APPLICATION_CREDENTIALS} airflow:/opt/airflow/key.json \
  && docker exec -u root airflow chown airflow:airflow key.json
```

#### Configure Airflow variables

In DAGs under this directory affects on GCP resources, and they are specified by default.

GCP resources accessed in DAGs is specified via Airflow variables, which can be created by helper script.

```bash
# Set GCP project ID
$ PROJECT=...

# Create config files (which is located in volume mounted on container)
$ python $(git rev-parse --show-toplevel)/gcp/helper/configure.py ${PROJECT}

# Update Airflow variables
$ docker exec airflow bash dags/config/update.sh
```

You can check all variables via [Airflow UI](http://localhost:8080/admin/variable/)

#### Configure Airflow connections

As the GCP project where BigQuery jobs run is designated by Airflow connections,
it is needed to set GCP project in connection `bigquery_default`.

```bash
# Delete default `bigquery_default`
$ airflow connections -d --conn_id bigquery_default

# Add `bigquery_default` with GCP project ID
$ PROJECT=...
$ airflow connections -a \
     --conn_id bigquery_default \
     --conn_type google_cloud_platform \
     --conn_extra '{
       "extra__google_cloud_platform__project": "'${PROJECT}'"
     }'
```

## DAGs

Available DAGs are listed below with required IAM roles.

DAG ID|description|IAM roles
:--|:--|:--
file_to_gcs|Generate file and upload it to Google Cloud Storage|roles/storage.admin

---

## Build API doc

```bash
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv run \
  make -C $(git rev-parse --show-toplevel)/gcp/docs html
```
