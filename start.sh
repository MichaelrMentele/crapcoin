#!/usr/bin/env bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
# Starting the server
echo "Start node..."
python manage.py runserver 0.0.0.0:$PORT
