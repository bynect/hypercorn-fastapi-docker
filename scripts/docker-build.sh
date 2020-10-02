#! usr/bin/env bash

set -e

tag="bynect/hypercorn-fastapi:$NAME"
DOCKERFILE="$NAME"

if [ "$NAME" == "latest" ]
then
    DOCKERFILE="python3.8"
fi

docker build -t "$tag" --file "./images/${DOCKERFILE}.dockerfile" "./images/"
