FROM python:latest
RUN apt-get update && apt-get -y install cron vim
WORKDIR app
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./AERData .
COPY AERApi .
WORKDIR AERApi
ENTRYPOINT ["cron", "-f"]

