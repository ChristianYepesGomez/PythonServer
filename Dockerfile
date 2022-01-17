FROM python:latest
RUN apt-get update && apt-get -y install cron vim
WORKDIR app
COPY crontab /etc/cron.d/crontab
COPY requirements.txt requirements.txt
RUN chmod 0644 /etc/cron.d/crontab
RUN pip3 install -r requirements.txt
COPY ./AERData .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
