
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

`USE_TCP`: Specify if using tcp connection. When set to True, `TCP_PORT` will be binded either to `BIND` or `INSECURE_BIND` depending on `USE_SSL`. Default True.

`USE_SSL`: Specify if using ssl connection. When set to True, `SSL_PORT` will be binded to `BIND`. Requires `KEYFILE`/`CERTFILE`/`CA_CERTS`. Default False.

`TCP_PORT`: TCP port to be used by tcp binds or as fallback in insecure bind for SSL binds. Default `80`.

`SSL_PORT`: SSL port to be used in ssl binds (HTTPS). Default `443`.

`HOST`: Host ip or path. Default `0.0.0.0`.

## License
Licensed under MIT License.

Based on [tiangolo/uvicorn-gunicorn-docker](https://github.com/tiangolo/uvicorn-gunicorn-docker)

[docker tags]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi/tags
[docker repo]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi
