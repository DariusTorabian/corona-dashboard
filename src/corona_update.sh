#!/usr/bin/env bash

dt=$(date '+%d/%m/%Y %H:%M:%S')
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python $DIR/get_and_clean_data.py
sleep 1s
python $DIR/db_update.py

echo "\nUpdate script run at: '$dt'"
