FROM python:3.6.4

ENV PYTHONUNBUFFERED 1

RUN mkdir /app/
WORKDIR /app/
ADD . /app/
COPY ./db.sqlite3 /app/

RUN pip3 install pipenv
RUN pipenv install --system

EXPOSE 8000
