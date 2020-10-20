FROM bynect/hypercorn-fastapi:python3.8-slim

ENV TCP_PORT=8000 WORKER_CLASS=trio USE_TCP=true

COPY ./app /app
