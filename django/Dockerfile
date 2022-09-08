# run this file with docker build .
# pull base image
FROM python:3.9

# set environment variables

# ensure console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1

# ensure python does not writte .pyc files
ENV PYTHONUNBUFFERED 1

# set working directory of the image
WORKDIR /code

# copy project folder inot working directory of the image
COPY django_development /code/

# install dependencies 
RUN pip install pipenv && pipenv install --system

