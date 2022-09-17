# Django Development

## Resources

* Django for Professionals Production websites with Python & Django (3.1) (William S. Vincent)

## Setup

1. Install Python 3

```
C:\>python --version
Python 3.9.7
```

2. Install Docker Desktop

```
C:\>docker --version
Docker version 20.10.17, build 100c701
```

3. Install pipenv (ensure python 3 is installed first)

```
pip install pipenv
```

4. Down load repository 
5. change directory ```cd Python/django```
6. on the command terminal (CMD) start the docker containers

```docker
docker-compose up -d --build
```

7. once docker finishes building confirm django working in browser

```http://localhost:8000/```