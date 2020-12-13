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

## DAG folders

name|description
:--|:--
[tutorial](tutorial)|DAGs using pure Airflow functions
[gcp](gcp)|DAGs using operators to access [Google Cloud Platform](https://cloud.google.com/gcp)

---

## Optional

To build API documents for each dag, create virtual environment with pipenv.

```bash
# pipenv
$ pip install pipenv

# create virtual environment
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv install --dev
```
