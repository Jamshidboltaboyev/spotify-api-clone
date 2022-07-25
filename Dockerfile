FROM python:3.8.10-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
DEV_MODE=local


RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip

COPY ./requirements/ /app/requirements/

RUN pip install -r /app/requirements/${DEV_MODE}.txt

COPY . .

