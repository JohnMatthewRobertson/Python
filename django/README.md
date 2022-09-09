# django_development

# resources 

* Django for Professionals Production websites with Python & Django (3.1) (William S. Vincent)

# virtual environment 

install pipenv 

```
pip install pipenv
```

virtual environment start 

```
D:\github_projects\Python\django\django_development>pipenv shell
Launching subshell in virtual environment...
Microsoft Windows [Version 10.0.19044.1949]
(c) Microsoft Corporation. All rights reserved.

(django_development-N3L5-HHl) D:\github_projects\Python\django\django_development>
```

virtual environment end

```
(django_development-N3L5-HHl) D:\github_projects\Python\django\django_development>exit

Aborted!

D:\github_projects\Python\django\django_development>
```

# python linters

flake8

```
flake8 ./django_development --exclude=.env > static_code_analysis_output/flake8_output.txt
```

pylint 

```
pylint ./django_development --ignore=.env > static_code_analysis_output/pylint_output.txt
```

safety

```
safety check > static_code_analysis_output/safety_output.txt
```

bandit

```
bandit -r ./django_development > static_code_analysis_output/bandit_output.txt
```



# django

install django

```
pipenv install django
```

start django project

```
django-admin startproject config .
```

migrate database

```
python manage.py migrate
```

run django test server

```
python manage.py runserver
```

create app

```
python manage.py startapp home
```

edit the app config

add new apps to ```config/settings.py``` under ```INSTALLED_APPS = []```

add new apps to ```config/urls.py``` under ```urlpatterns = []```

edit the app home

add a new file ```urls.py``` 

update ```views.py```

# docker 

create Dockerfile 

build docker image 

```
docker build .
```

control container that uses docker image

create docker-compose.yaml

start container in detached mode (-d)

```
docker-compose up -d
```

view logs 

```
docker-compose logs
```

confirm working 

http://127.0.0.1:8000/ or http://localhost:8000/ 



docker-compose exec <service_name> not container name

and also must be run from same directory as docker-compose.yaml

creaete super user on docker container 

```
docker-compose exec django python manage.py createsuperuser
```

install postgres python plugin into container

```
docker-compose exec django pipenv install psycopg2
```

rebuild container

```
docker-compose up -d --build
```

migarte database 

```
docker-compose exec django python manage.py migrate
```


create admin user for database

```
docker-compose exec django python manage.py createsuperuser
```

add custom user model to docker

```
docker-compose exec django python manage.py startapp accounts
```

acccounts

change ```models.py```

config

change ```settings.py```

migrate database 

```
docker-compose exec django python manage.py makemigrations accounts
```

```
docker-compose exec django python manage.py migrate
```

docker tests

```
docker-compose exec django python manage.py test
```