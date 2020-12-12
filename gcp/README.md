# gcp

<!-- TOC -->

- [gcp](#gcp)
    - [Usage](#usage)
        - [Setup docker container](#setup-docker-container)
            - [Create config file](#create-config-file)
            - [Start container](#start-container)
        - [Setup credential](#setup-credential)
            - [Copy key file](#copy-key-file)
    - [DAGs](#dags)
    - [Build api doc](#build-api-doc)

<!-- /TOC -->

## Usage

### Setup docker container

#### Create config file

In DAGs under this directory affects on GCP resources, and they are not specified by default.

GCP resources accessed in DAGs is specified via config files, which can be created by helper script.

```bash
# DAG ID whose GCP configuration to be modified
$ DAG_ID=...

$ python $(git rev-parse --show-toplevel)/gcp/helper/configure.py ${DAG_ID}
```

Available DAG IDs are listed [here](#DAGs).

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

### Setup credential

Following operations assume accessing GCP project using an service account.
Before proceeding,

1. Create service account, and grant proper privileges to the account (see [below](#dags))
1. Download service account key file

#### Copy key file

Copy service account key file to docker container.

```bash
# GOOGLE_APPLICATION_CREDENTIALS=/path/to/key/file.json
$ docker cp ${GOOGLE_APPLICATION_CREDENTIALS} airflow:/opt/airflow/key.json \
  && docker exec -u root airflow chown airflow:airflow key.json
```

## DAGs

Available DAGs are listed below with required IAM roles.

DAG ID|description|IAM roles
:--|:--|:--
file_to_gcs|Generate file and upload it to Google Cloud Storage|roles/storage.admin

## Build api doc

```bash
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv run \
  make -C $(git rev-parse --show-toplevel)/gcp/docs html
```
