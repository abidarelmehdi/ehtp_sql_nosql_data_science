# pull official base image
FROM python:3.8-slim-buster

# install dependencies
COPY requirements/requirements.txt .
RUN pip install pip -U
RUN pip install --no-cache-dir -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .
RUN python manage.py collectstatic