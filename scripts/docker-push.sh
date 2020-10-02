#! usr/bin/env bash

set -e

use_tag="bynect/hypercorn-fastapi:$NAME"

bash scripts/docker-build.sh
bash scripts/docker-login.sh

docker push "$use_tag"
