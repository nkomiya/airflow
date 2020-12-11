# demo

## Prerequisite

Build docker image according to branch [emulator](https://github.com/nkomiya/airflow/tree/emulator).

### Additional task

To build airflow DAGs correctly, update git submodules.

```bash
# checkout demo branch
$ git checkout demo

# update submodule
$ git submodule update -i
```

## DAGs

name|dag folder|description
:--|:--|:--
[quick_start](quick_start)|[quick_start/dags](https://github.com/nkomiya/airflow/blob/demo/quick_start/dags)|A simple dag by [Apache Airflow's tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)

---

## Optional

To build API documents for each dag, create virtual environment with pipenv.

```bash
# pipenv
$ pip install pipenv

# create virtual environment
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv install --dev
```
