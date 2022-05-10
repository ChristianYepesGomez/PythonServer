FROM python:latest
RUN apt-get update && apt-get -y install vim
WORKDIR app
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./ .
WORKDIR AERApi

