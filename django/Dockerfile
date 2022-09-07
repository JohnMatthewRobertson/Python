# run this file with docker build .
# pull base image
FROM python:3.9

# set environment variables

# ensure console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1

# ensure python does not writte .pyc files
ENV PYTHONUNBUFFERED 1

# set working directory within image
WORKDIR /code

# install dependencies
COPY django_development/Pipfile django_development/Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# copy project
COPY django_development /code/
