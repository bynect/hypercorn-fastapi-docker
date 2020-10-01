#! usr/bin/env bash

set -e

use_tag="bynect/hypercorn-fastapi:$NAME"

DOCKERFILE="$NAME"

if [ "$NAME" == "latest" ]
then
    DOCKERFILE="python3.8"
fi

docker build -t "$use_tag" --file "./images/${DOCKERFILE}.dockerfile" "./images/"
