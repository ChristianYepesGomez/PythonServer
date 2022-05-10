FROM python:latest
RUN apt-get update && apt-get -y install cron vim
WORKDIR spiders
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./ .
RUN ["chmod", "+x", "./scripts/crawl.sh"]
WORKDIR AERData
ENTRYPOINT ["cron", "-f"]

