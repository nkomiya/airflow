# demo

## Prerequisite

Build docker image according to [emulator](https://github.com/nkomiya/airflow/tree/emulator) branch.

### Additional task

To build airflow DAGs correctly, update git submodules.

```bash
# checkout demo branch
$ git checkout demo

# update submodule
$ git submodule update -i
```

## DAGs

DAG ID|description
:--|:--
[quick_start](quick_start)|A simple DAG by [Apache Airflow's tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
[gcp](gcp)|Sample DAGs which access to [Google Cloud Platform](https://cloud.google.com/gcp)

---

## Optional

To build API documents for each dag, create virtual environment with pipenv.

```bash
# pipenv
$ pip install pipenv

# create virtual environment
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv install --dev
```
