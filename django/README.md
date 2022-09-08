# django_development

```
C:\>docker --version
Docker version 20.10.17, build 100c701
```

```
C:\>python --version
Python 3.9.7
```

## resources 

* Django for Professionals Production websites with Python & Django (3.1) (William S. Vincent)

black, autopep8, yapf, pylint, flake8, bandit, safety

https://github.com/wsvincent/djangoforprofessionals

virtualenv , venv , pipenv


https://pypi.org/project/pipenv/
pip install pipenv

pipenv install django

virtual environment start 

```
D:\github_projects\Python\django\django_development>pipenv shell
Launching subshell in virtual environment...
Microsoft Windows [Version 10.0.19044.1949]
(c) Microsoft Corporation. All rights reserved.

(django_development-N3L5-HHl) D:\github_projects\Python\django\django_development>
```

start django project

django-admin startproject config .


python manage.py migrate

python manage.py runserver

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 07, 2022 - 21:02:12
Django version 4.1.1, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

control+c

create app

python manage.py startapp home

config

add new apps to config/settings.py under INSTALLED_APPS = []

add new apps to config/urls.py under urlpatterns = []

home

add a new file urls.py 

update views.py

virtual environment end

```
(django_development-N3L5-HHl) D:\github_projects\Python\django\django_development>exit

Aborted!

D:\github_projects\Python\django\django_development>
```

create Dockerfile 

build docker image 

docker build .

control container that uses docker image

create docker-compose.yaml

start container in detached mode (-d)

docker-compose up -d

view logs 

docker-compose logs

confirm working 

http://127.0.0.1:8000/ or http://localhost:8000/ 



docker-compose exec <service_name> not container name

stop container control+c or docker-compose down

creaete super user on docker container 

```
docker-compose exec django_container python /code/django_development/manage.py createsuperuser
```

install postgres python plugin into container

docker-compose exec django pipenv install psycopg2

rebuild container

docker-compose up -d --build

migarte database 

docker-compose exec django_container python manage.py migrate

docker-compose exec django_container python /code/django_development/manage.py createsuperuser



