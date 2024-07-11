# To run: docker run -v /path/to/wsgi.py:/var/www/datamodelutils/wsgi.py --name=datamodelutils -p 81:80 datamodelutils
# To check running container: docker exec -it datamodelutils /bin/bash

FROM ubuntu:xenial-20201014

ENV DEBIAN_FRONTEND=noninteractive

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
    python3.6 \
    python-dev \
    python-pip \
    python-setuptools \
    sudo \
    vim \
    && pip install pip==9.0.3 \
    && pip install --upgrade setuptools

COPY . /datamodelutils
WORKDIR /datamodelutils
RUN pwd

RUN pip install -r requirements.txt
RUN pip install .
