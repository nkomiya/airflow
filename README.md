# airflow

## Build

```bash
cd $(git rev-parse --show-toplevel) \
  && docker build -t airflow .
```

## Usage

Put all files in $(pwd)/dags to container's dags directory.

```bash
docker run -d --rm -p 8080:8080 --volume $(pwd)/dags:/opt/airflow/dags airflow
```
