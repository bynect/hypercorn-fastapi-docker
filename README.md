
![Deploy](https://github.com/bynect/hypercorn-fastapi/workflows/Deploy/badge.svg?branch=main)

## Image tags and Dockerfiles

- [`python3.8`, `latest`](images/python3.8.dockerfile)
- [`python3.8-slim`](images/python3.8-slim.dockerfile)
- [`python3.8-alpine`](images/python3.8-alpine.dockerfile)
- [`python3.7`](images/python3.7.dockerfile)
- [`python3.7-slim`](images/python3.7-slim.dockerfile)
- [`python3.7-alpine`](images/python3.7-alpine.dockerfile)

# hypercorn-fastapi

Docker image with [Hypercorn][hypercorn site] for [FastAPI][fastapi site] application in Python 3.7+. With slim and alpine options.

### Hypercorn
**[Hypercorn][hypercorn site]** is an HTTP2 ready ASGI web server based on the sans-io hyper, h11, h2, and wsproto libraries and inspired by Gunicorn.

Hypercorn supports HTTP/1, HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI/2, and ASGI/3 specifications. Hypercorn can utilise asyncio, uvloop, or trio worker types.

### FastAPI
**[FastAPI][fastapi site]** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- Fast to code: Increase the speed to develop features by about 300% to 500% *.
- Less bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Less bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

<small>* estimation based on tests on an internal development team, building production applications.</small>

## How to use
- You can use this image as a base image for other images, using this in your Dockerfile:
```docker
FROM bynect/hypercorn-fastapi:python3.8-slim

COPY ./app /app
```
It will expect a file either at `/app/app/main.py` or `/app/main` containing the variable `app` containing your FastAPI application.

Then you can build you Dockerfile, e.g:
```sh
$ docker build -t myimage ./
```

# Usage
## Environment variables

`USE_TCP`: Specify if using tcp connection. When set to True, `TCP_PORT` will be binded either to `BIND` or `INSECURE_BIND` depending on `USE_SSL`. Default True.

`USE_SSL`: Specify if using ssl connection. When set to True, `SSL_PORT` will be binded to `BIND`. Requires `KEYFILE`/`CERTFILE`/`CA_CERTS`. Default False.

`TCP_PORT`: TCP port to be used by tcp binds or as fallback in insecure bind for SSL binds. Default `80`.

`SSL_PORT`: SSL port to be used in ssl binds (HTTPS). Default `443`.

`HOST`: Host ip or path. Default `0.0.0.0`.

## Hypercorn configuration file
The image includes a default Gunicorn Python config file at `/hypercorn_conf.py`.

You can it by including a file in:
- `/app/app/hypercorn_conf.py`
- `/app/hypercorn_conf.py`
- `/hypercorn_conf.py`

<small>* ordered by priority.</small>

Alternatively you can set the environmental variable `HYPERCORN_CONF` to the configuration file path.  
Note that `HYPERCORN_CONF` needs the prefix `file:` for Python file, `python:` for Python module and no prefix for TOML file.

## Prestart script
If you need to run anything before starting the app, you can add a file prestart.sh to the directory `/app`.
The image will automatically detect and run it before starting everything.
If you need to run a Python script before starting the app, you could make the /app/prestart.sh file run your Python script, with something like:

```sh
#! /usr/bin/env bash

# Run custom Python script before starting
python /app/my_custom_prestart_script.py
```
You can customize the location of the prestart script with the environment variable `PRE_START_PATH` described above.

---

## License
Licensed under MIT License.

Based on [tiangolo/uvicorn-gunicorn-docker](https://github.com/tiangolo/uvicorn-gunicorn-docker)

[docker tags]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi/tags
[docker repo]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi

[fastapi site]: https://fastapi.tiangolo.com/
[hypercorn site]: https://pgjones.gitlab.io/hypercorn/
