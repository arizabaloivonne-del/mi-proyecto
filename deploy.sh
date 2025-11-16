# Script de arranque para Railway

#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
gunicorn webVentas.wsgi:application --bind 0.0.0.0:$PORT
