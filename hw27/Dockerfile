
FROM python:3.9.5-slim-buster

RUN pip install django

COPY ./tutorial /app
WORKDIR /app

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
