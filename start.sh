#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn school_deployee.wsgi:application --bind 0.0.0.0:$PORT