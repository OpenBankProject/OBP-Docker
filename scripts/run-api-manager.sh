#!/bin/sh
cd /code
cp -rf /tmp/local_settings.py /code/apimanager/apimanager/local_settings.py
pip install -r requirements.txt
cd /code/apimanager
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000