
![Deploy](https://github.com/bynect/hypercorn-fastapi/workflows/Deploy/badge.svg?branch=main)

## Image tags and Dockerfiles

- [`python3.8`, `latest`](images/python3.8.dockerfile)
- [`python3.8-slim`](images/python3.8-slim.dockerfile)
- [`python3.8-alpine`](images/python3.8-alpine.dockerfile)
- [`python3.7`](images/python3.7.dockerfile)
- [`python3.7-slim`](images/python3.7-slim.dockerfile)
- [`python3.7-alpine`](images/python3.7-alpine.dockerfile)

**Note**: Every image has additional [tags][docker tags] made in every build date. E.g. `bynect/hypercorn-fastapi:python3.8-2020-10-01`.

# hypercorn-fastapi

Use FastAPI with Hypercorn, a super-fast and HTTP2 ready ASGI web server inspired by Gunicorn.

## Usage

`TCP_PORT`: TCP port to be used by tcp binds or as insecure bind for SSL binds. Default `80`.
`HOST`: Host ip or path. Default `0.0.0.0`.

## License
Licensed under MIT License.

Based on [tiangolo/uvicorn-gunicorn-docker](https://github.com/tiangolo/uvicorn-gunicorn-docker)

[docker tags]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi/tags
[docker repo]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi
