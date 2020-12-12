# tutorial

<!-- TOC -->

- [tutorial](#tutorial)
    - [Usage](#usage)
        - [Setup docker container](#setup-docker-container)
    - [DAGs](#dags)
        - [Tasks](#tasks)
            - [quick_start](#quick_start)
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

### Tasks

#### quick_start

Task ID|description
:--|:--
print_date|output current time
sleep|sleep 1 second
templated|sample task using templated command

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
