# pull base image
FROM python:3.9

# ensure console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1

# ensure python does not writte .pyc files
ENV PYTHONUNBUFFERED 1

# set working directory of the image
WORKDIR /code

# copy project folder into working directory of the image
COPY django_development /code/

# upgrade pip
RUN pip install --upgrade pip

# install pipenv and install existing pipfile into environment
RUN pip install pipenv && pipenv install --system

