FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
# RUN apt install -y postgresql

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && apt-get install -y tzdata

RUN apt-get update

COPY requirements.txt /opt/source_code/requirements.txt
COPY . /opt/source_code/
WORKDIR /opt/source_code

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "app.py" ]
