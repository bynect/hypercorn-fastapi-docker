FROM python:3.8-slim

LABEL author="bynect <bynect@gmail.com>"

RUN python3 -m pip install hypercorn hypercorn[uvloop] hypercorn[trio] trio aioquic hypercorn[h3] fastapi \
    --no-cache-dir --no-color --no-python-version-warning --disable-pip-version-check

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./hypercorn_conf.py /hypercorn_conf.py

COPY ./app /app

WORKDIR /app
ENV PYTHONPATH=/app

EXPOSE 80
EXPOSE 443

CMD ["/start.sh"]
