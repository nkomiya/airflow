from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = "dags/config/variables.conf"


def get_default_if_empty(val, default):
    return val if val != "" else default


def update_config(config, section, **kwds):
    config.add_section(section)
    for k, v in kwds.items():
        config.set(section, k, v)


def main():
    p = ArgumentParser(description="Update configuration")
    p.add_argument("project", type=str, help="GCP project ID")
    args = p.parse_args()

    # GCP project ID
    project = args.project

    # update configuration
    gcs_bucket = input(f"GCS bucket name used in DAGs: [{project}-airflow]: ").strip()
    gcs_bucket = get_default_if_empty(gcs_bucket, f"{project}-airflow")

    bq_project = input(f"BigQuery project used in DAGs: [{project}]: ").strip()
    bq_project = get_default_if_empty(bq_project, project)

    bq_dataset = input("BigQuery dataset used in DAGs: []: ").strip()
    bq_dataset = get_default_if_empty(bq_dataset, "")

    # build
    config = ConfigParser()
    update_config(config, "gcp", gcs_bucket=gcs_bucket, bq_project=bq_project, bq_dataset=bq_dataset)
    with open(CONFIG, "w") as f:
        config.write(f)


if __name__ == "__main__":
    main()
