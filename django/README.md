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

## Setup (Django App in Docker)

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

```
docker-compose exec --workdir /code django flake8 ./django_development --exclude=.env > ../static_code_analysis_output/flake8_output.txt
```

### linters (Django App in Docker)

1. flake8:

```
docker-compose exec --workdir /code django flake8 ./django_development --exclude=.env > ../static_code_analysis_output/flake8_output.txt
```

3. pylint:

```
docker-compose exec --workdir /code django pylint ./django_development --ignore=.env > ../static_code_analysis_output/pylint_output.txt
```

3. bandit:

```
docker-compose exec --workdir /code django bandit -r ./django_development > ../static_code_analysis_output/bandit_output.txt
```

4. safety:

```
docker-compose exec --workdir /code django safety check > ../static_code_analysis_output/safety_output.txt
```

### Tests (Django App in Docker)

1. run coverage 

```
docker-compose exec django coverage run --source="." manage.py test
```

2. produce coverage report

```
docker-compose exec django coverage report > ./static_code_analysis_output/coverage_output.txt
```

### Static Asserts

1. 

```
docker-compose exec django python manage.py collectstatic
```

## Setup (Django App test server / virtual environment)
## Requires Docker PostGres database to be running

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

4. on the command line run:

```
python manage.py makemigrations
```

5. on the command line run:

```
python manage.py migrate
```

6. on the command line run:

```
python manage.py createsuperuser
```

7. run the django test server

```
python manage.py runserver 4444
```

8. check in browser to access 

```
http://127.0.0.1:4444
```

### linters (Django App test server / virtual environment)

1. change directory: 

```
cd Python/django
```

2. flake8:

```
flake8 ./django_development --exclude=.env > static_code_analysis_output/flake8_output.txt
```

3. pylint:

```
pylint ./django_development --ignore=.env > static_code_analysis_output/pylint_output.txt
```

3. bandit:

```
bandit -r ./django_development > static_code_analysis_output/bandit_output.txt
```

4. safety:

```
safety check > ./static_code_analysis_output/safety_output.txt
```

### Tests (Django App test server / virtual environment)

1. change directory: 

```
cd Python/django/django_development
```

2. run coverage 

```
coverage run --source="." manage.py test
```

3. produce coverage report

```
coverage report > ../static_code_analysis_output/coverage_output.txt
```

### Static Asserts

1. change directory: 

```
cd Python/django/django_development
```

2. 

```
python manage.py collectstatic
```