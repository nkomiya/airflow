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
            - [branching](#branching)
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

Available DAGs are listed below.

DAG ID|description
:--|:--
quick_start|A simple DAG for quick start
xcom_single|Share single object between PythonOperators using XCom
xcom_kv|Share multiple keyed objects between PythonOperators using XCom

### Tasks

Available tasks in each DAG are listed below.

#### quick_start

Task ID|description
:--|:--
print_date|output current time
sleep|sleep 1 second
templated|sample task using templated command
branching|branch workflow depending on whether run date is weekdays or not

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

#### branching

Task ID|description
:--|:--
branch_op|branch workflow depending on run date
on_weekdays|task to be executed on weekdays
on_weekends|task to be executed on weekends

To test the DAG, run back fill for a certain period.

```bash
# Run back fill for 1 week
$ airflow backfill -s 2020-01-01 -e 2020-01-07 branching
```

You can check workflow branching on [Airflow UI](http://localhost:8080/admin/airflow/tree?dag_id=branching).

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
