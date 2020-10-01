FROM python:3.8-slim

LABEL author="bynect <bynect@gmail.com>"

RUN pip install fastapi hypercorn[uvloop] hypercorn[trio] \
    --no-cache-dir --no-color --no-python-version-warning --disable-pip-version-check

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./hypercorn_conf.py /hypercorn_conf.py

COPY ./app /app

WORKDIR /app
ENV PYTHON_PATH=/app

EXPOSE 80
EXPOSE 443

CMD ["/start.sh"]
