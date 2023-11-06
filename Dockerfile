FROM python:3.10.4-slim-bullseye
EXPOSE 8080

WORKDIR /app
RUN pip3 install --upgrade pip

COPY requirements.txt /app
RUN pip3 install -r ./requirements.txt

COPY . /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
