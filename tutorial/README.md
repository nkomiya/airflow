# tutorial

<!-- TOC -->

- [tutorial](#tutorial)
    - [Usage](#usage)
        - [Setup docker container](#setup-docker-container)
    - [DAGs](#dags)
        - [Tasks](#tasks)
            - [quick_start](#quick_start)
            - [xcom_single](#xcom_single)
            - [xcom_kv](#xcom_kv)
    - [Testing](#testing)
    - [Build API doc](#build-api-doc)

<!-- /TOC -->

## Usage

### Setup docker container

Activate Airflow web UI on [localhost](http://localhost:8080).

```bash
# start container
$ docker run -d --rm --name airflow -p 8080:8080 \
    --volume $(git rev-parse --show-toplevel)/tutorial/dags:/opt/airflow/dags \
    airflow

# set alias
$ alias airflow='docker exec airflow airflow'
```

## DAGs

Available DAGs are listed below with required IAM roles.

DAG ID|description
:--|:--
quick_start|A simple DAG for quick start
xcom_single|Share single object between PythonOperators using XCom
xcom_kv|Share multiple keyed objects between PythonOperators using XCom

### Tasks

#### quick_start

Task ID|description
:--|:--
print_date|output current time
sleep|sleep 1 second
templated|sample task using templated command

#### xcom_single

Task ID|description
:--|:--
xcom_push|push single value
xcom_pull|pull single value

#### xcom_kv

Task ID|description
:--|:--
xcom_push|push multiple keyed objects
xcom_pull|pull multiple keyed objects

## Testing

Tasks in a DAG can be executed by `airflow test` command.
Usage of this command is as follow.

```bash
# DAG_ID  : ID of DAG to be tested
# TASK_ID : ID of task to be tested
# RUN_DATE: Run date of DAG, format is YYYY-mm-dd
$ airflow test ${DAG_ID} ${TASK_ID} ${RUN_DATE}
```

If you want to dry-run a task, add `-dr` option.

```bash
# run task with dry run
$ airflow test -dr quick_start print_date 2020-01-01
```

---

## Build API doc

```bash
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv run \
  make -C $(git rev-parse --show-toplevel)/tutorial/docs html
```
