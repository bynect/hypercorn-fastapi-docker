#! usr/bin/env bash

set -e

tag="bynect/hypercorn-fastapi:$NAME"

bash scripts/docker-build.sh
bash scripts/docker-login.sh

docker push "$tag"
