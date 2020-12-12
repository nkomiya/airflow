from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = "dags/config/variables.conf"


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
    gcs_bucket = input(f"GCS bucket name used in DAGS: [{project}-airflow]: ").strip()
    gcs_bucket = gcs_bucket if gcs_bucket != "" else f"{project}-airflow"

    # build
    config = ConfigParser()
    update_config(config, "gcp", gcs_bucket=gcs_bucket)
    with open(CONFIG, "w") as f:
        config.write(f)


if __name__ == "__main__":
    main()
