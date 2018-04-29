FROM python:3.6.4

# Copy over code files
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod 664 /app

# Install python packages
RUN pip3 install pipenv
RUN pipenv install --dev --system
RUN pipenv install --system

# Create fresh db
RUN rm -f -- db.sqlite3
RUN touch db.sqlite3
RUN python manage.py migrate

ENV PYTHONUNBUFFERED 1

# Default port number for entrypoint
ENV PORT=8000

# Optional arguments for configuring Sauron/non-sauron nodes
ENV SAURON_URL=http://localhost:8999


EXPOSE $PORT

ENTRYPOINT ["/app/start.sh"]
