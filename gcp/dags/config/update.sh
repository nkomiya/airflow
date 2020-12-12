#!/bin/bash

cd $(dirname $0) || exit 1

cmd=$(
    awk '
        BEGIN { gcp = 0 }

        # check section
        {
            if ($1 ~ /^\[.*\]/) {
                if ($1 ~ /gcp/) {
                    gcp = 1
                } else {
                    gcp = 0
                }
                next
            }
        }

        # variable update commands
        {
            if (gcp) {
                sub(" ", "")
                sub("=", "")
                if ($1 != "") print("airflow variables -s " $0 ";")
            }
        }
    ' variables.conf
)

eval ${cmd}
