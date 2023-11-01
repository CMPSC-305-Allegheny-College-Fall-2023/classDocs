# Commands for setting up Django boilerplate code

## Create a virtual environment

* mkdir ~/djangoWorking/
* cd ~/djangoWorking/
* python3 -m venv myvenv
* source myvenv/bin/activate

## Install libraries

* pip install django
* pip install --upgrade pip

## Initiate Django

* django-admin startproject mysite
* cd mysite
* python3 manage.py runserver 
* url; http://localhost:8000/
* python3 manage.py migrate

## Establish a superuser as a project admin

* python3 manage.py createsuperuser
  * usr: you@allegheny.edu
  * passwd: thisIsIt#2
