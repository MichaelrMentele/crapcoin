FROM python:3.6.4

ENV PYTHONUNBUFFERED 1

# Default port number for entrypoint
ENV PORT=8000

# Optional arguments for configuring Sauron/non-sauron nodes
ENV IS_SAURON=False
ENV SAURON_URL=http://localhost:8999

# Copy over code files
RUN mkdir /app
WORKDIR /app
ADD . /app

# Create fresh db
RUN rm -f -- db.sqlite3
RUN touch db.sqlite3

RUN pip3 install pipenv
RUN pipenv install --system

EXPOSE $PORT

ENTRYPOINT ["/app/start.sh"]
