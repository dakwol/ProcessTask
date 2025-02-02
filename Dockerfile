FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ProcessTask.settings

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
