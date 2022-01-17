FROM python:latest
WORKDIR app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY AERData .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
