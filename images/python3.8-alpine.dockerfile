FROM python:3.8-alpine

LABEL author="bynect <bynect@gmail.com>"

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install fastapi hypercorn[uvloop] hypercorn[trio] \
    --no-cache-dir --no-color --no-python-version-warning --disable-pip-version-check \
    && apk del .build-deps gcc libc-dev make

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./hypercorn_conf.py /hypercorn_conf.py

COPY ./app /app

WORKDIR /app
ENV PYTHON_PATH=/app

EXPOSE 80
EXPOSE 443

CMD ["/start.sh"]
