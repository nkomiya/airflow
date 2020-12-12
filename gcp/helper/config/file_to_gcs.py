import os
from configparser import ConfigParser

# default values
SRC_PATH = "/opt/airflow/work/temp.txt"
DST_BUCKET = ""
DST_OBJECT = ""

# sections in conf file
SECTIONS = ["src", "dst"]


def update(path, detail):
    parser = ConfigParser()

    if os.path.exists(path):
        parser.read(path)

    for s in SECTIONS:
        if not parser.has_section(s):
            parser.add_section(s)

    # detailed setting
    if detail:
        f = input(f"Temporary file path [{SRC_PATH}]: ").strip()
        parser["src"]["path"] = f if f != "" else SRC_PATH
    else:
        # set default if blank
        if not parser.has_option("src", "path"):
            parser["src"]["path"] = SRC_PATH

    v = input(f"Output GCS bucket name [{DST_BUCKET}]: ").strip()
    parser["dst"]["bucket"] = v

    v = input(f"Output GCS object name [{DST_OBJECT}]: ").strip()
    parser["dst"]["name"] = v

    # output to file
    with open(path, "w") as f_obj:
        parser.write(f_obj)
