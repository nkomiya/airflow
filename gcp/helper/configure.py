from argparse import ArgumentParser
from configparser import ConfigParser
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT.joinpath("dags/config/variables.conf")


def update(config, section, option, prompt, default):
    default = config.get(section, option, fallback=default)
    val = input(f"{prompt} [{default}] > ").strip()
    val = val if val != "" else default
    config.set(section, option, val)


def main():
    p = ArgumentParser(description="Update configuration")
    p.add_argument("-d", "--delete", action="store_true", default=False, help="Delete config file")
    p.add_argument("-p", "--project", type=str, default=None, help="GCP project ID")
    args = p.parse_args()

    if args.delete:
        if os.path.exists(CONFIG):
            os.remove(CONFIG)
        return

    if args.project is None:
        p.error("GCP project ID should be designated by option `-p`.")

    # read config file if exists
    config = ConfigParser()
    if os.path.exists(CONFIG):
        config.read(CONFIG.as_posix())
    else:
        config.add_section("gcp")

    # GCP project ID
    project = args.project
    # update configuration
    update(config, "gcp", "gcs_bucket", "GCS bucket name used in DAGs", f"{project}-airflow")
    update(config, "gcp", "bq_project", "BigQuery project used in DAGs", project)
    update(config, "gcp", "bq_dataset", "BigQuery dataset used in DAGs", "")

    # output
    with open(CONFIG, "w") as f:
        config.write(f)


if __name__ == "__main__":
    main()
