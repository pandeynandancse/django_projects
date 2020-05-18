FROM python:3.8



RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENV port 8000

ENTRYPOINT  ["python"]

CMD ["manage.py", "runserver"]
