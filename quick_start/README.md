# quick-start

## Start airflow

Activate Airflow web UI on [localhost](http://localhost:8080).

```bash
$ docker run -d --rm --name airflow -p 8080:8080 \
    --volume $(git rev-parse --show-toplevel)/quick_start/dags:/opt/airflow/dags \
    airflow
```

## Testing

```bash
# set alias
$ alias airflow='docker exec airflow airflow'

# run task with dry run
$ airflow test -dr quick_start print_date 2020-01-01
```

## Build api doc

```bash
$ PIPENV_PIPFILE=$(git rev-parse --show-toplevel)/Pipfile pipenv run \
  make -C $(git rev-parse --show-toplevel)/quick_start/docs html
```
