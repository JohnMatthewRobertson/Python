# Django Development

## Resources

* Django for Professionals Production websites with Python & Django (3.1) (William S. Vincent)

## Prerequisite

1. Install Docker Desktop:

* https://www.docker.com/products/docker-desktop/

docker desktop version:

```
C:\>docker --version
Docker version 20.10.17, build 100c701
```

2. Install Python 3:

* https://www.python.org/downloads/

```
C:\>python --version
Python 3.9.7
```

3. Install pipenv: 

* https://pypi.org/project/pipenv/

```
C:\>pip show pipenv
Name: pipenv
Version: 2022.9.4
Summary: Python Development Workflow for Humans.
Home-page: https://github.com/pypa/pipenv
Author: Pipenv maintainer team
Author-email: distutils-sig@python.org
License: MIT
Location: d:\python3_9_7\lib\site-packages
Requires: certifi, setuptools, virtualenv, virtualenv-clone
Required-by:
```

4. Down load repository. 

## Setup (run Django App in Docker)

1. change directory: 

```
cd Python/django
```

2. on the command terminal (CMD) start the docker containers:

```docker
docker-compose up -d --build
```

3. on the command terminal (CMD) run the following command: 

```
docker-compose exec django python manage.py makemigrations
```

4. on the command terminal (CMD) run the following command:

```
docker-compose exec django python manage.py migrate
```

5. on the command terminal (CMD) run the following command:

```
docker-compose exec django python manage.py createsuperuser
```

6. once docker finishes building confirm django working in browser

```
http://localhost:8000/
```

7. once docker finishes building confirm pgadmin working in browser

```
http://localhost:5050/
```

## Setup (run Django App test server)

1. change directory: 

```
cd Python/django/django_development
``` 

2. start virtual environment 

```
pipenv shell
```

3. install dependencies 

```
pipenv install
```

4. run the django test server

```
python manage.py runserver 4444
```

5. check in browser to access 

```
http://127.0.0.1:4444
```

