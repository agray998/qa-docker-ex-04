FROM python:3.8

COPY . .

RUN pip3 install flask flask-sqlalchemy

ENTRYPOINT python3 main.py
