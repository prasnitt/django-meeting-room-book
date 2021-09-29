# django-meeting-room-book

Following the Pluralsight https://app.pluralsight.com/library/courses/django-getting-started/table-of-contents
The Github link for course material: https://github.com/codesensei-courses/django_getting_started 


## instllation instructions
    pip install -r requirements.txt

## Setups
    django-admin startproject <project name>

    python manage.py startapp <new app name> 

## Run
Run server

    python manage.py runserver

## Auth

Create super user

    python manage.py createsuperuser


## Database

Make migrations

    python manage.py makemigrations

Show pending migrations

    python manage.py showmigrations

Get SQL statement for migration

    python manage.py sqlmigrate <app> <migration number>

Apply migration

    python manage.py migrate

Connect to Data base using shell

    python manage.py dbshell


## Format
    black .