# Dokku Django Starter Template

Starter template for pushing projects to dokku

## Features

Staticfiles served by whitenoise
Uses gunicorn
Database environment variable, if not present use local sqlite3. Change to your needs.

## Tutorial

1. Create your virtual environment
2. Install Django (`$ pip install django`)
3. django-admin.py startproject --template {url} --name=myproject

## Deploying

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ git remote add dokku dokku@yourip.net:myproject
    $ git push dokku master

    On your dokku server:
    $ dokku postgresql:create mydb
    $ dokku postgresql:link myapp mydb
    $ dokku run myproject python manage.py migrate