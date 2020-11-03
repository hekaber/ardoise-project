FROM python:3

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    python-pydot python-pydot-ng graphviz graphviz-dev\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY docker/django/requirements.txt ./
RUN pip install -r requirements.txt
COPY ardoise-serv/ .
