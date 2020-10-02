#! /usr/bin/env sh

set -e

if [ -f /app/main.py ]
then
    DEFAULT_MODULE=main
fi

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE}
APP_NAME=${APP_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$APP_NAME"}

HOST=${HOST:-0.0.0.0}
TCP_PORT=${TCP_PORT:-80}
BIND=${BIND:-"$HOST:$TCP_PORT"}

LOG_LEVEL=${LOG_LEVEL:-info}

PRE_START_PATH=${PRE_START_PATH:-/app/prestart.sh}
if [ -f $PRE_START_PATH ]
then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no script $PRE_START_PATH"
fi

exec hypercorn --debug --reload --bind $BIND --log-level $LOG_LEVEL "$APP_MODULE"
