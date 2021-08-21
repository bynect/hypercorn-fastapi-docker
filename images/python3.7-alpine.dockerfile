FROM python:3.7-alpine

LABEL author="bynect <bynect@gmail.com>"

RUN apk add --no-cache --virtual .build-deps gcc libc-dev libffi-dev openssl-dev \
    build-base bsd-compat-headers make musl-dev python3-dev cargo \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install hypercorn hypercorn[uvloop] hypercorn[trio] trio aioquic hypercorn[h3] fastapi \
    --no-cache-dir --no-color --no-python-version-warning --disable-pip-version-check \
    && apk del .build-deps gcc libc-dev make

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
