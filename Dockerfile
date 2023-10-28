FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

COPY app /app

WORKDIR /app

EXPOSE 8000

RUN adduser --disabled-password app-user

USER app-user