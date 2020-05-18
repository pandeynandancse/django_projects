FROM python:3.8


WORKDIR /app

COPY . /app


RUN pip install -r requirements.txt





ENV port 8000

ENTRYPOINT  ["python"]

CMD ["manage.py", "runserver"]
