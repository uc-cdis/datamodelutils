# To run: docker run -v /path/to/wsgi.py:/var/www/datamodelutils/wsgi.py --name=datamodelutils -p 81:80 datamodelutils
# To check running container: docker exec -it datamodelutils /bin/bash

FROM quay.io/cdis/python:python3.9-buster-2.0.0

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    # dependency for cryptography
    libffi-dev \
    # dependency for pyscopg2 - which is dependency for sqlalchemy postgres engine
    libpq-dev \
    # dependency for cryptography
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    python3.9 \
    python-dev \
    python-pip \
    python-setuptools \
    sudo \
    vim

COPY . /datamodelutils
WORKDIR /datamodelutils
RUN pwd

RUN pip install --upgrade pip && pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -vv
