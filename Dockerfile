FROM python:3.10 as base

ENV PYTHONUNBUFFERED=1

RUN pip install pipenv

WORKDIR /usr/local/src/webapp/src/

COPY . ./

RUN pipenv install --system --deploy

