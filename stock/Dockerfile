# pull oficial base image
FROM python:3.8-slim-buster

# set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFERRED 1

# set work directory
WORKDIR /app

# copy/install dependencies
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

CMD python manage.py runserver 0.0.0.0:8011