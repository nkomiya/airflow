from argparse import ArgumentParser
from pathlib import Path

import config


ROOT = Path(__file__).resolve().parent.parent
PY_FILES = "helper/config/*.py"
CONF_DIR = "dags/config"


def main():
    # list of DAGs
    dags = list(map(lambda x: x.stem, filter(lambda x: x.name != "__init__.py", ROOT.glob(PY_FILES))))

    p = ArgumentParser(description="Update configuration")
    p.add_argument("dag", choices=dags, help="DAG name to be configured")
    p.add_argument("-d", "--detail", action="store_true", default=False, help="Enable detailed configuration")
    args = p.parse_args()

    # update configuration
    dag = args.dag
    path = ROOT.joinpath(CONF_DIR).joinpath(dag + ".conf")
    getattr(config, dag).update(path, args.detail)


if __name__ == "__main__":
    main()
