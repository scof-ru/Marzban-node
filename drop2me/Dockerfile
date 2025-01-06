# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /code

COPY src /code
RUN pip3 install -r /code/requirements.txt

CMD [ "bash", "-c", "python main.py"]
