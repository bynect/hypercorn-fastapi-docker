
![Deploy](https://github.com/bynect/hypercorn-fastapi/workflows/Deploy/badge.svg?branch=main)

## Image tags and Dockerfiles

* [`python3.8`, `latest`](images/python3.8.dockerfile)
* [`python3.8-slim`](images/python3.8-slim.dockerfile)
* [`python3.8-alpine`](images/python3.8-alpine.dockerfile)
* [`python3.7`](images/python3.7.dockerfile)
* [`python3.7-slim`](images/python3.7-slim.dockerfile)
* [`python3.7-alpine`](images/python3.7-alpine.dockerfile)

# hypercorn-fastapi

Docker image with [Hypercorn][hypercorn site] for [FastAPI][fastapi site] application in Python 3.7+. With slim and alpine options.

* **[Github repo][github repo]**
* **[Docker hub][docker repo]**

### Hypercorn
**[Hypercorn][hypercorn site]** is an HTTP2 ready ASGI web server based on the sans-io hyper, h11, h2, and wsproto libraries and inspired by Gunicorn.

Hypercorn supports HTTP/1, HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI/2, and ASGI/3 specifications. Hypercorn can utilise asyncio, uvloop, or trio worker types.

### FastAPI
**[FastAPI][fastapi site]** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+.

The key features are:

* Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
* Fast to code: Increase the speed to develop features by about 300% to 500% *.
* Less bugs: Reduce about 40% of human (developer) induced errors. *
* Intuitive: Great editor support. Completion everywhere. Less time debugging.
* Easy: Designed to be easy to use and learn. Less time reading docs.
* Short: Minimize code duplication. Multiple features from each parameter declaration. Less bugs.
* Robust: Get production-ready code. With automatic interactive documentation.
* Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

<small>* estimation based on tests on an internal development team, building production applications.</small>

## How to use
* You can use this image as a base image for other images, using this in your Dockerfile:

```dockerfile
FROM bynect/hypercorn-fastapi:python3.8-slim

COPY ./app /app
```
It will expect a file either at `/app/app/main.py` and `/app/main` containing the variable `app` containing your FastAPI application.

Then you can build you Dockerfile, e.g:
```sh
$ docker build -t myimage ./
```

# Usage
## Environment variables
These are the environment variables that you can set in the container to configure it and their default values.
You can set alternative values for them either from shell or from Dockerfile, e.g:
```sh
#from shell
$ docker run -d -p 80:80 -e MODULE_NAME="custom_app.custom_main" myimage
```
```dockerfile
#from Dockerile
FROM bynect/hypercorn-fastapi:python3.8-slim

ENV MODULE_NAME="custom_app.custom_main"

COPY ./app /app
```


#### `MODULE_NAME`

The Python "module" (file) to be imported by Hypercorn, this module would contain the actual application in a variable.

By default:

* `app.main` if there's a file `/app/app/main.py` or
* `main` if there's a file `/app/main.py`

For example, if your main file was at `/app/custom_app/custom_main.py`, you could set it like:

```sh
$ docker run -d -p 80:80 -e MODULE_NAME="custom_app.custom_main" myimage
```


#### `VARIABLE_NAME`

The variable inside of the Python module that contains the FastAPI application.

By default:

* `app`

For example, if your main Python file has something like:

```python
from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def read_root():
    return {"Hello": "World"}
```

In this case `api` would be the variable with the FastAPI application. You could set it like:

```sh
$ docker run -d -p 80:80 -e VARIABLE_NAME="api" myimage
```


#### `APP_MODULE`

The string with the Python module and the variable name passed to Hypercorn.

By default, set based on the variables `MODULE_NAME` and `VARIABLE_NAME`:

* `app.main:app` or
* `main:app`

You can set it like:

```sh
$ docker run -d -p 80:80 -e APP_MODULE="custom_app.custom_main:api" myimage
```


#### `HYPERCORN_CONF`

The path to a Hypercorn Python configuration file.

By default:

* `/app/app/hypercorn_conf.py` if file exists
* `/app/hypercorn_conf.py` if file exists
* `/hypercorn_conf.py` included file

<small>* ordered by priority.</small>

You can set it like:

```sh
$ docker run -d -p 80:80 -e GUNICORN_CONF="/app/custom_gunicorn_conf.py" myimage
```

**Note**: that `HYPERCORN_CONF` needs the prefix `file:` for Python file, `python:` for Python module and no prefix for TOML file.


#### `WORKERS_PER_CORE`

This image will check how many CPU cores are available in the current server running your container.

It will set the number of workers to the number of CPU cores multiplied by this value.

By default:

* `1`

You can set it like:

```sh
$ docker run -d -p 80:80 -e WORKERS_PER_CORE="3" myimage
```

If you used the value `3` in a server with 2 CPU cores, it would run 6 worker processes.

You can use floating point values too.

So, for example, if you have a big server (let's say, with 8 CPU cores) running several applications, and you have a FastAPI application that you know won't need high performance. And you don't want to waste server resources. You could make it use `0.5` workers per CPU core. For example:

```sh
$ docker run -d -p 80:80 -e WORKERS_PER_CORE="0.5" myimage
```

In a server with 8 CPU cores, this would make it start only 4 worker processes.


#### `MAX_WORKERS`

Set the maximum number of workers to use.

You can use it to let the image compute the number of workers automatically but making sure it's limited to a maximum.

This can be useful, for example, if each worker uses a database connection and your database has a maximum limit of open connections.

By default it's not set, meaning that it's unlimited.

You can set it like:

```sh
$ docker run -d -p 80:80 -e MAX_WORKERS="24" myimage
```

This would make the image start at most 24 workers, independent of how many CPU cores are available in the server.


#### `WEB_CONCURRENCY`

Override the automatic definition of number of workers.

By default:

* Set to the number of CPU cores in the current server multiplied by the environment variable `WORKERS_PER_CORE`. So, in a server with 2 cores, by default it will be set to `2`.

You can set it like:

```sh
$ docker run -d -p 80:80 -e WEB_CONCURRENCY="2" myimage
```

This would make the image start 2 worker processes, independent of how many CPU cores are available in the server.


#### `HOST`

The "host" used by Hypercorn, the IP where Hypercorn will listen for requests.

It is the host inside of the container.

So, for example, if you set this variable to `127.0.0.1`, it will only be available inside the container, not in the host running it.

It's is provided for completeness, but you probably shouldn't change it.

By default:

* `0.0.0.0`


#### `TCP_PORT`

The tcp port the container should listen on when `USE_TCP` is set to true.

If you are running your container in a restrictive environment that forces you to use some specific port (like `8080`) you can set it with this variable.

By default:

* `80`

You can set it like:

```sh
$ docker run -d -p 80:8080 -e TCP_PORT="8080" myimage
```


#### `USE_SSL`

If Hypercorn will use ssl-related options. When false ssl-related options are not used.

By default is set to:
* `false`

>Depends on `CA_CERTS` - `CERTFILE` - `KEYFILE`
>At least one of `USE_SSL` and `USE_TCP` **MUST** be set to true.


#### `USE_TCP`

If Hypercorn will use tcp-related options. When false tcp-related options are not used.

By default is set to:
* `true`

>At least one of `USE_SSL` and `USE_TCP` **MUST** be set to true.


#### `SSL_PORT`

The ssl port the container should listen on when `USE_SSL` is set to true.

If you are running your container in a restrictive environment that forces you to use some specific port (like `8000`) you can set it with this variable.

By default:

* `443`

You can set it like:

```sh
$ docker run -d -p 443:8000 -e SSL_PORT="8000" myimage
```
>Depens on `USE_SSL`


#### `BIND`

The actual host and port passed to Hypercorn.

If `USE_SSL` is set to true the default value will be based on `HOST` and `SSL_PORT`.
So, if you didn't change anything, it will be set by default to:

* `0.0.0.0:443`

Otherwise, if `USE_SSL` is not set to true, the value will be based on `HOST` and `TCP_PORT`.
So, if you didn't change anything, it will be set by default to:

* `0.0.0.0:80`

You can set it like:

```sh
$ docker run -d -p 80:8080 -e BIND="0.0.0.0:8080" myimage
```


#### `INSECURE_BIND`

The host and port passed to Hypercorn as fallback in HTTPS connections.

If `USE_SSL` and `USE_TCP` are both true the default value is based on the variables `HOST` and `TCP_PORT`.

So, if you didn't change anything, it will be set by default to:

* `0.0.0.0:80`

Otherwise, if `USE_SSL` is not set to true or `USE_TCP` is set to false, the value will be set to `None`.

You can manually set only when the aforementioned conditions are true.
>Depens on `USE_SSL` and `USE_TCP`

#### `QUIC_BIND`

Quic bind to be used instead of bind. By default it's not set.

You can set it like:

```sh
$ docker run -d -p 80:8080 -e QUIC_BIND="0.0.0.0:8080" myimage
```


#### `LOG_LEVEL`

The log level for Hypercorn.

One of:

* `debug`
* `info`
* `warning`
* `error`
* `critical`

By default, set to `info`.

If you need to squeeze more performance sacrificing logging, set it to `warning`, for example:

You can set it like:

```sh
$ docker run -d -p 80:8080 -e LOG_LEVEL="warning" myimage
```

#### `WORKER_CLASS`

The worker class to be used by Hypercorn.

By default, set to `asyncio`.

The three avaible values are:
* `asyncio`
* `uvloop`
* `trio`

You can set it like:

```sh
$ docker run -d -p 80:8080 -e WORKER_CLASS="uvloop" myimage
```


#### `CA_CERTS`

Path to CA certificate file. By default it's not set.

>Depends on `USE_SSL`


#### `CERTFILE`

Path to CA certificate file. By default it's not set.

>Depends on `USE_SSL`


#### `KEYFILE`

Path to CA certificate file. By default it's not set.

>Depends on `USE_SSL`


#### `CIPHERS`

Ciphers used by ssl connection. By default:
* `"ECDHE+AESGCM"`

>Depends on `USE_SSL`


#### `KEEP_ALIVE`

The number of seconds to wait for requests on a Keep-Alive connection.

By default, set to `5`.

You can set it like:

```sh
$ docker run -d -p 80:8080 -e KEEP_ALIVE="20" myimage
```


#### `GRACEFUL_TIMEOUT`

Timeout for graceful workers restart.

By default, set to `120`.

You can set it like:

```sh
$ docker run -d -p 80:8080 -e GRACEFUL_TIMEOUT="20" myimage
```


#### `ACCESS_LOG`

The access log file to write to.

By default `"-"`, which means stdout (print in the Docker logs).

If you want to disable `ACCESS_LOG`, set it to an empty value.

For example, you could disable it with:

```sh
$ docker run -d -p 80:8080 -e ACCESS_LOG= myimage
```


#### `ERROR_LOG`

The error log file to write to.

By default `"-"`, which means stderr (print in the Docker logs).

If you want to disable `ERROR_LOG`, set it to an empty value.

For example, you could disable it with:

```sh
$ docker run -d -p 80:8080 -e ERROR_LOG= myimage
```


#### `BACKLOG`

The maximum number of pending connections. By default set to `100`.


#### `PRE_START_PATH`

The path where to find the pre-start script.

By default, set to `/app/prestart.sh`.

You can set it like:

```sh
$ docker run -d -p 80:8080 -e PRE_START_PATH="/custom/script.sh" myimage
```


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


## Hypercorn configuration

The image includes a default Gunicorn Python config file at /gunicorn_conf.py.
It uses the environment variables declared above to set all the configurations.

You can override it by including a file in:

* `/app/app/hypercorn_conf.py`
* `/app/hypercorn_conf.py`
* `/hypercorn_conf.py`

<small>* ordered by priority.</small>

## Development live reload
The default program that is run is at `/start.sh`. It does everything described above.

There's also a version for development with live auto-reload at:

`/start-reload.sh`
#### Details
For development, it's useful to be able to mount the contents of the application code inside of the container as a Docker "host volume", to be able to change the code and test it live, without having to build the image every time.

In that case, it's also useful to run the server with live auto-reload, so that it re-starts automatically at every code change.

The additional script `/start-reload.sh` runs Hypercorn with 1 `asyncio` worker.

It is ideal for development.

#### Usage
For example, instead of running:

```sh
$ docker run -d -p 80:80 myimage
```
You could run:
```sh
$ docker run -d -p 80:80 -v $(pwd):/app myimage /start-reload.sh
```
* `-v $(pwd):/app`: means that the directory `$(pwd)` should be mounted as a volume inside of the container at `/app`.
* `$(pwd)`: runs pwd ("print working directory") and puts it as part of the string.
* `/start-reload.sh`: adding something (like `/start-reload.sh`) at the end of the command, replaces the default "command" with this one. In this case, it replaces the default (`/start.sh`) with the development alternative `/start-reload.sh`.

#### Development live reload - Technical Details
As `/start-reload.sh` runs Hypercorn for debug/development purpose it doesn't use hypercorn_config file.

But these environment variables will work the same as described above:

* `MODULE_NAME`
* `VARIABLE_NAME`
* `APP_MODULE`
* `HOST`
* `TCP_PORT` (only tcp avaible)
* `LOG_LEVEL`


### Falsy/Truly value

The included `/hypercorn_conf.py` has some options that accepts boolean value.
These are the valid values. Invalid values will raise an exception.

Falsy values (compared after lowered):
* `"no"`
* `"n"`
* `"0"`
* `"false"`
  
Truly values (compared after lowered):
* `"yes"`
* `"y"`
* `"1"`
* `"true"`


## License
Licensed under MIT License.

Based on [tiangolo/uvicorn-gunicorn-docker](https://github.com/tiangolo/uvicorn-gunicorn-docker)

[docker tags]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi/tags
[docker repo]: https://hub.docker.com/repository/docker/bynect/hypercorn-fastapi
[github repo]: https://github.com/bynect/hypercorn-fastapi-docker
[fastapi site]: https://fastapi.tiangolo.com/
[hypercorn site]: https://pgjones.gitlab.io/hypercorn/
