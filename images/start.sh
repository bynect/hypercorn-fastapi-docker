#! /usr/bin/env sh

set -e

if [ -f /app/main.py ]
then
    DEFAULT_MODULE=main
fi

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE}
APP_NAME=${APP_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$APP_NAME"}

if [ -f /app/hypercorn_conf.py ]
then
    DEFAULT_CONF=file:/app/hypercorn_conf.py
else
    DEFAULT_CONF=file:/hypercorn_conf.py
fi

export HYPERCORN_CONF=${HYPERCORN_CONF:-$DEFAULT_CONF}

export WORKER_CLASS=${WORKER_CLASS:-"asyncio"}

PRE_START_PATH=${PRE_START_PATH:-/app/prestart.sh}
if [ -f $PRE_START_PATH ]
then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no script $PRE_START_PATH"
fi

exec hypercorn -k "$WORKER_CLASS" -c "$HYPERCORN_CONF" "$APP_MODULE"
